import json
import pika


def callback(ch, method, properties, body):

    message = json.loads(body)

    print("Received:", message)


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