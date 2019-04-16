#!/usr/bin/env python3
import pika
print(' [*] TUVIEJA')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))

print(' [*] TUVIEJA2')
channel = connection.channel()

print(' [*] TUVIEJA3')

channel.queue_declare(queue='hello')

print(' [*] TUVIEJA4')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

print(' [*] TUVIEJA5')

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()