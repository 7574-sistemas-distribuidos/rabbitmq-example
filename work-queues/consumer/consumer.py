#!/usr/bin/env python3
import pika
import time
import os

consumer_id = os.environ["CONSUMER_ID"]
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('[{}] Waiting for messages. To exit press CTRL+C'.format(consumer_id))


def callback(ch, method, properties, body):
    print("[{}] Received {}".format(consumer_id, body))
    time.sleep(body.count(b'.'))
    print("[{}] Done".format(consumer_id))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()