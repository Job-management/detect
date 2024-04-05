from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from venv import logger
import pika
import json

app = FastAPI(title="Get job information from post")
from ai import detect

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestBody(BaseModel):
    """
    Class request body
    """

    text: str
    images: list = []
    type: str = None


class RequestBodyEvent(BaseModel):
    """
    Class request body
    """

    event: str


class DataResponse:
    def __init__(self, code: str, message: str, data: str):
        self.code = code
        self.message = message
        self.data = data


@app.get("/whoami")
def check():
    try:
        return "I'm service detect data (gemini AI)"
    except Exception as e:
        print(e)
        logger.error(f"Error occurred while handle data: {e}")


@app.post("/data")
def data(request: RequestBody):
    print("========= PROCESSING =========")
    try:
        if not request.text:
            raise HTTPException(status_code=400, detail="Text field is required")
        if not request.type:
            raise HTTPException(status_code=400, detail="Type field is required")
        data = detect(request.text)
        response = DataResponse(code=200, message="SUCCESS", data=json.loads(data))
        return response
    except Exception as e:
        logger.error(f"Error occurred while handle data: {e}")
        return e


@app.post("/push-data")
def pushData(req: Request):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq", blocked_connection_timeout=300)
        )
        channel = connection.channel()

        channel.queue_declare(queue="raw-data")
        channel.basic_publish(
            exchange="",
            routing_key="raw-data",
            body="[DANANG] Meta Technology Lab vẫn cần tuyển Middle/Senior từ 3 năm+ kinh nghiệm về tham gia dự án game bùng nổ tháng 5/2024\n1. Project manager\n2. Middle Blockchain\n3. Senior Cloud infrastructure\n4. Senior Unreal Engine\nMức offer upto 3k5 cho các ứng viên tiềm năng cùng các trải nghiệm dự án\nLiên hệ:\nMail: hr@metatechnologylab.io\nZalo: 0336 256 356\nSkype: live:.cid.7d8bc6574e23c88b",
        )
        channel.close()
    except Exception as e:
        logger.error(f"Error occurred while handle data: {e}")


def consume_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="raw-data")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue="raw-data", on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

    # Start consuming messages in a separate process
    consumer_process = multiprocessing.Process(target=consume_queue)
    consumer_process.start()


@app.post("/event")
def event_listener(request: RequestBodyEvent):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="raw-data")
    try:
        if not request.event:
            raise HTTPException(status_code=400, detail="Event field is required")
        event = request.event

        def callback(ch, method, properties, body):
            print(f" [x] Received {body}")

        if event == "HANDLE_DATA_IN_QUEUE":

            channel.basic_consume(
                queue="raw-data", on_message_callback=callback, auto_ack=True
            )
            channel.start_consuming()

    except Exception as e:
        logger.error(f"Error occurred while event processing: {e}")
