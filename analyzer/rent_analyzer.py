from src.models.database import get_connection
from src.models.analysis_repository import save_analysis


def analyze_city(city):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            price,
            square_feet
        FROM rental_listings
        WHERE city = %s
    """, (city,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        return

    prices = [float(row[0]) for row in rows]

    avg_rent = sum(prices) / len(prices)

    highest_rent = max(prices)

    lowest_rent = min(prices)

    listing_count = len(prices)

    rent_per_sqft_values = []

    for row in rows:

        price = row[0]
        sqft = row[1]

        if sqft:
            rent_per_sqft_values.append(
                float(price) / float(sqft)
            )

    avg_rent_per_sqft = 0

    if rent_per_sqft_values:
        avg_rent_per_sqft = (
            sum(rent_per_sqft_values)
            / len(rent_per_sqft_values)
        )

    save_analysis(
        city,
        avg_rent,
        avg_rent_per_sqft,
        highest_rent,
        lowest_rent,
        listing_count
    )