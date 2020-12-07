FROM python:3.9.0-alpine3.12

RUN pip install pika

ADD *.py /app/

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["publisher.py"]
