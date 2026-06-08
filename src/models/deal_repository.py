from src.models.database import get_connection


def save_undervalued_property(
        listing_id,
        expected_rent,
        actual_rent,
        savings):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO undervalued_properties
        (
            listing_id,
            expected_rent,
            actual_rent,
            savings
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
    """,
    (
        listing_id,
        expected_rent,
        actual_rent,
        savings
    ))

    conn.commit()

    cur.close()
    conn.close()