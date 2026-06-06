from faker import Faker
import random

from src.models.database import get_connection

fake = Faker()


def collect_rental_data():

    conn = get_connection()
    cur = conn.cursor()

    address = fake.street_address()

    city = random.choice([
        "Arlington",
        "Dallas",
        "Fort Worth",
        "Irving"
    ])

    price = random.randint(1000, 3000)

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
            'Collector',
            %s,
            %s,
            'TX',
            '76010',
            %s
        )
    """,
    (
        address,
        city,
        price
    ))

    conn.commit()

    cur.close()
    conn.close()

    print("Listing collected")


for _ in range(10):
    collect_rental_data()