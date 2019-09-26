#!/usr/bin/env python3
import pika
import sys
import random
import time

# Wait for rabbitmq to come up
time.sleep(10)

# Create RabbitMQ communication channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()


channel.queue_declare(queue='task_queue', durable=True)

for i in range(100):
    message = "." * random.randint(1,11)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)
    time.sleep(1)

connection.close()