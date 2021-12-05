import json

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='app2')

def publish(body):
    channel.basic_publish(exchange='',
                          routing_key='app2',
                          body=json.dumps(body))