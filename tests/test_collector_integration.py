from Collector.collector import collect_rental_data
from src.models.database import get_connection


def test_collector_inserts_listing():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM rental_listings"
    )

    before_count = cur.fetchone()[0]

    collect_rental_data()

    cur.execute(
        "SELECT COUNT(*) FROM rental_listings"
    )

    after_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    assert after_count == before_count + 1