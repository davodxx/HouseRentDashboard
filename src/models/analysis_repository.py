from src.models.database import get_connection


def save_analysis(
        city,
        avg_rent,
        avg_rent_per_sqft,
        highest_rent,
        lowest_rent,
        listing_count):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO rent_analysis
        (
            city,
            avg_rent,
            avg_rent_per_sqft,
            highest_rent,
            lowest_rent,
            listing_count
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """,
    (
        city,
        avg_rent,
        avg_rent_per_sqft,
        highest_rent,
        lowest_rent,
        listing_count
    ))

    conn.commit()

    cur.close()
    conn.close()