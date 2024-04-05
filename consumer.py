import pika
from ai import detect

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()

channel.queue_declare(queue="raw-data")

def verifyData(json_data):
    
    return json_data;


def callback(ch, method, properties, body):
    print("=================")
    message_body = body.decode("utf-8")
    json_data = detect(message_body)
    print(str(json_data))
    print("=================")


channel.basic_consume(queue="raw-data", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
