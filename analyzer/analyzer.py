import json
import pika


from analyzer.rent_analyzer import analyze_city
from analyzer.deal_finder import find_undervalued_properties



def callback(ch, method, properties, body):

    message = json.loads(body)

    print("Received:", message)

    cities = [
        "Arlington",
        "Dallas",
        "Fort Worth",
        "Irving"
    ]

    for city in cities:
        analyze_city(city)

        find_undervalued_properties(city)

    print("Analysis completed")


connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(
    queue="rental_analysis_queue",
    durable=True
)

channel.basic_consume(
    queue="rental_analysis_queue",
    on_message_callback=callback,
    auto_ack=True
)

print("Analyzer waiting...")

channel.start_consuming()