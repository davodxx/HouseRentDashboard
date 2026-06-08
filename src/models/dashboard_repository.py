from src.models.database import get_connection


def get_dashboard_stats():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM rental_listings
    """)

    total_listings = cur.fetchone()[0]

    cur.execute("""
        SELECT AVG(price)
        FROM rental_listings
    """)

    average_rent = round(float(cur.fetchone()[0]), 2)

    cur.execute("""
        SELECT MAX(price)
        FROM rental_listings
    """)

    highest_rent = round(float(cur.fetchone()[0]), 2)

    cur.execute("""
        SELECT MIN(price)
        FROM rental_listings
    """)

    lowest_rent = round(float(cur.fetchone()[0]), 2)

    cur.close()
    conn.close()

    return {
        "total_listings": total_listings,
        "average_rent": average_rent,
        "highest_rent": highest_rent,
        "lowest_rent": lowest_rent
    }

def get_city_analysis():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            city,
            avg_rent,
            highest_rent,
            lowest_rent,
            listing_count
        FROM rent_analysis
        ORDER BY city
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def get_best_deals():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            rental_listings.address,
            rental_listings.city,
            undervalued_properties.actual_rent,
            undervalued_properties.expected_rent,
            undervalued_properties.savings
        FROM undervalued_properties
        JOIN rental_listings
            ON rental_listings.id =
               undervalued_properties.listing_id
        ORDER BY savings DESC
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows