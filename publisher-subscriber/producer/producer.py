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

channel.exchange_declare(exchange='logs', exchange_type='fanout')

for i in range(100):
    message = "Random number FTW: {}".format(random.randint(1,11))
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(1)

connection.close()