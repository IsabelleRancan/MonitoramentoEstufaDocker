import pika
import json

def send_to_queue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='dados_criticos')

    message = json.dumps(data)
    channel.basic_publish(exchange='', routing_key='dados_criticos', body=message)
    connection.close()
