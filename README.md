# 🌱 Monitoramento de Estufa com Microsserviços e Mensageria (RabbitMQ) utilizando Docker

Este projeto simula um sistema de monitoramento de uma estufa utilizando dois microsserviços desenvolvidos em Python, com troca de mensagens via RabbitMQ e envio de alertas por e-mail. Todo o serviço está em containers se comunicando em uma rede docker.

---

## 🧩 Estrutura do Projeto
```text
MonitoramentoEstufa/
│
├── email_service/
│   ├── consumer.py
│   ├── Dockerfile
│   ├── email_sender.py
│   └── requirements.txt
│
├── monitor_service/
│   ├── app.py
│   ├── db.py
│   ├── Dockerfile
│   ├── estufa.db
│   ├── models.py
│   ├── rabbitmq.py
│   └── requirements.txt
│
├── .env.example
├── .gitignore
├── Atividade FINAL - PROVA.pdf
├── comandos.txt
├── docker-compose.yml
├── README.md

```

- `monitor_service/`: Serviço responsável por receber dados e enviá-los ao banco e fila
- `email_service/`: Serviço que consome mensagens da fila e envia e-mails de alerta
- `docker-compose.yml`: Arquivo para orquestrar os containers

---

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** — criação da API REST
- **SQLAlchemy** — ORM para banco de dados
- **SQLite** — banco de dados leve e local
- **RabbitMQ + pika** — mensageria entre os microsserviços
- **smtplib + email** — envio de e-mail real via SMTP
- **Docker / Docker Compose** - contêinerização com Docker

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/IsabelleRancan/MonitoramentoEstufaDocker.git
cd MonitoramentoEstufaDocker
```

### 2. Configure as variáveis de ambiente
- Renomeie o arquivo .env.example para .env
- Preencha com suas credenciais de e-mail (usar senha de app para Gmail)

```text
RABBITMQ_HOST=rabbitmq
EMAIL_REMETENTE=seu_email@gmail.com
SENHA_APP=sua_senha_de_aplicativo
EMAIL_DESTINO=email_para_alerta@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

## 🐋 Construção e Inicialização dos Serviços

> Com o aplicativo **Docker Desktop** já instalado e configurado em seu dispositivo:

### 1. Rode os containers
Em um terminal:
``` bash
docker-compose up --build
```
> Você pode consultar alguns comandos úteis no arquivo `comandos.txt` deste projeto.

---

## 🧪 Testando a Aplicação

### Enviar dados com Postman
POST http://localhost:5000/transmit
``` json 
{
  "temperatura": 60,
  "sensacao_termica": 68,
  "umidade": 10
}
```
Se os dados forem críticos, um e-mail será enviado! 📬
O serviço de e-mail ficará escutando a fila e enviando os alertas automaticamente.

---

## 📌 Endpoints da API

| Método | Rota            | Descrição                                   |
| ------ | --------------- | ------------------------------------------- |
| GET    | `/all`          | Retorna todos os registros de monitoramento |
| GET    | `/critical`     | Retorna apenas os dados críticos            |
| POST   | `/transmit`     | Cria um novo registro de monitoramento      |

---

## 🛡️ Segurança
- Informações sensíveis como senhas não estão no código
- .env está no .gitignore
- .env.example mostra como configurar variáveis sem risco

---

## 🔍 Úteis

- Desenvolvido por Isabelle Firmino Rancan — Estudante de Análise e Desenvolvimento de Sistemas – IFMS
- Projeto desenvolvido como atividade final de Aplicações Distrubuídas.
- [Vídeo com exemplo de uso e explicação do ambiente Docker](https://drive.google.com/file/d/18xn8sj2suomm52Yltzqf4LUT2ZJITkuM/view?usp=sharing)