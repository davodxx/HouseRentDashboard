from src.models.database import get_connection


def get_all_listings():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            address,
            city,
            price
        FROM rental_listings
        ORDER BY id DESC
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def create_listing(
        address,
        city,
        state,
        zip_code,
        price):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO rental_listings
        (
            source,
            address,
            city,
            state,
            zip_code,
            price
        )
        VALUES
        (
            'Manual Entry',
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """,
    (
        address,
        city,
        state,
        zip_code,
        price
    ))

    conn.commit()

    cur.close()
    conn.close()