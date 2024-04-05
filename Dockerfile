FROM python:3.9

WORKDIR /app/handler-data

COPY ./requirements.txt .

RUN pip install -q -U google-generativeai
RUN pip install --no-cache-dir --upgrade -r /app/handler-data/requirements.txt
