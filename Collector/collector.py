import json
import pika
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

    # Publish RabbitMQ message

    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )

    channel = connection.channel()

    channel.queue_declare(
        queue="rental_analysis_queue",
        durable=True
    )

    channel.basic_publish(
        exchange="",
        routing_key="rental_analysis_queue",
        body=json.dumps({
            "event": "new_rental_data"
        })
    )
    print("Message published to rabbit MQ")

    connection.close()

    cur.close()
    conn.close()

    print("Listing saved to database")


for _ in range(5):
    collect_rental_data()