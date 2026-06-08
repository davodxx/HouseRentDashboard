from src.models.database import get_connection


def test_rent_analysis_exists():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM rent_analysis
    """)

    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    assert count >= 0