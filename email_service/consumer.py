import pika
import json
import os
import time
from email_sender import enviar_email

def callback(ch, method, properties, body):
    dados = json.loads(body)
    print("📥 Mensagem recebida da fila!")
    enviar_email(dados)

def main():
    rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
    print(f"🖨️ Conectando ao RabbitMQ em: {rabbitmq_host}")

    # Tenta se conectar por até 10 tentativas (espera 5s entre elas)
    for i in range(10):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            break  # sucesso na conexão, sai do loop
        except pika.exceptions.AMQPConnectionError as e:
            print(f"❌ Tentativa {i+1}/10: RabbitMQ ainda não disponível, tentando novamente em 5s...")
            time.sleep(5)
    else:
        print("💀 Não foi possível conectar ao RabbitMQ após várias tentativas.")
        return

    channel = connection.channel()
    channel.queue_declare(queue='dados_criticos')

    channel.basic_consume(queue='dados_criticos',
                          on_message_callback=callback,
                          auto_ack=True)

    print("👂 Aguardando mensagens na fila 'dados_criticos'. Para sair, pressione CTRL+C.")
    channel.start_consuming()

if __name__ == '__main__':
    main()
