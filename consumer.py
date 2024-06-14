import pika
from ai import detect
from DB import save_data_into_DB
import json

print("===== START CONSUMER =====")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
channel = connection.channel()

channel.queue_declare(queue="raw-data")


def verifyData(json_data):

    return json_data


def callback(ch, method, properties, body):
    try:
        print("=================")
        message_body = body.decode("utf-8")
        dict_message = json.loads(message_body)
        print(dict_message)
        data = detect(dict_message)
        print(data)
        if(data == "null"): return
        dict_data = json.loads(data)

        # Kiểm tra xem dict_data có phải là một danh sách không
        if isinstance(dict_data, list):
            for _data in dict_data:
                save_data_into_DB(_data)
        else:
            save_data_into_DB(dict_data)
    except Exception as e:
        print(e)


channel.basic_consume(queue="raw-data", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
