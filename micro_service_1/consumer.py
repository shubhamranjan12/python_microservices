import functools
import threading
import pika

NO_OF_CONSUMERS = 30
threads = list()


def initializer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', heartbeat=0))
    channel = connection.channel()
    channel.queue_declare(queue='app2')
    return channel


def callback(ch, method, properties, body, args):
    # Do stuff here when a message is received from service-name
    print(f"Service-1: Received in consumer-{args['name']} {body}")


def handle(name):
    channel = initializer()
    print(f'Service-1: Worker-{name} Started consuming messages')
    arg = {'name': name}
    on_message_callback = functools.partial(callback, args=(arg))
    channel.basic_consume('app2', on_message_callback)
    channel.start_consuming()


for i in range(NO_OF_CONSUMERS):
    consumer = threading.Thread(target=handle, args=(i,))
    threads.append(consumer)
    consumer.start()