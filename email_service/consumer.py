import pika
import json
from email_sender import enviar_email

def callback(ch, method, properties, body):
    dados = json.loads(body)
    print("📥 Mensagem recebida da fila!")
    enviar_email(dados)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='dados_criticos')
    channel.basic_consume(queue='dados_criticos',
                          on_message_callback=callback,
                          auto_ack=True)

    print("👂 Aguardando mensagens na fila 'dados_criticos'. Para sair, pressione CTRL+C.")
    channel.start_consuming()

if __name__ == '__main__':
    main()
