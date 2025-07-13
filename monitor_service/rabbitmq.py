import pika
import json
import os

def send_to_queue(data):
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'rabbitmq')  # padrão: 'rabbitmq'
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue='dados_criticos')

    message = json.dumps(data)
    channel.basic_publish(exchange='', routing_key='dados_criticos', body=message)
    connection.close()
