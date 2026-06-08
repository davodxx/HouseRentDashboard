from src.models.database import get_connection
from src.models.deal_repository import save_undervalued_property


def find_undervalued_properties(city):

    conn = get_connection()
    cur = conn.cursor()

    # Get average rent

    cur.execute("""
        SELECT AVG(price)
        FROM rental_listings
        WHERE city = %s
    """, (city,))

    average_rent = cur.fetchone()[0]

    if average_rent is None:

        cur.close()
        conn.close()
        return

    # Get listings

    cur.execute("""
        SELECT
            id,
            price
        FROM rental_listings
        WHERE city = %s
    """, (city,))

    listings = cur.fetchall()

    for listing in listings:

        listing_id = listing[0]
        actual_rent = float(listing[1])

        if actual_rent < float(average_rent):

            savings = float(average_rent) - actual_rent

            save_undervalued_property(
                listing_id,
                average_rent,
                actual_rent,
                savings
            )

    cur.close()
    conn.close()