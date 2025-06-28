# 🌱 Monitoramento de Estufa com Microsserviços e Mensageria (RabbitMQ)

Este projeto simula um sistema de monitoramento de uma estufa utilizando dois microsserviços desenvolvidos em Python, com troca de mensagens via RabbitMQ e envio de alertas por e-mail.

---

## 🧩 Estrutura do Projeto
```text
MonitoramentoEstufa/
│
├── email_service/
│   ├── .env.example
│   ├── consumer.py
│   └── email_sender.py
│
├── monitor_service/
│   ├── app.py
│   ├── db.py
│   ├── estufa.db
│   ├── models.py
│   └── rabbitmq.py
│
├── .gitignore
├── Atividade 3.pdf
├── README.md
├── requirements.txt
```

---

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** — criação da API REST
- **SQLAlchemy** — ORM para banco de dados
- **SQLite** — banco de dados leve e local
- **RabbitMQ + pika** — mensageria entre os microsserviços
- **smtplib + email** — envio de e-mail real via SMTP
- **dotenv** — leitura de variáveis de ambiente

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/IsabelleRancan/MonitoramentoEstufa.git
cd MonitoramentoEstufa
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o envio de e-mails
- Renomeie o arquivo .env.example para .env dentro da pasta email_service/
- Preencha com suas credenciais de e-mail (usar senha de app para Gmail)

```text
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA=sua_senha_de_aplicativo
EMAIL_DESTINO=destinatario@gmail.com
```

---

## ▶️ Execução dos Microsserviços

### 1. Inicie o monitoramento da estufa
Em um terminal:
``` bash
cd monitor_service
python app.py
```
API rodando em: http://localhost:5000

### 2. Inicie o consumidor de mensagens
Em outro terminal:
``` bash
cd email_service
python consumer.py
```

---

## 🧪 Testando a Aplicação

### Enviar dados com Postman
POST http://localhost:5000/transmit
``` json 
{
  "temperatura": 55,
  "sensacao_termica": 68,
  "umidade": 45
}
```
Se os dados forem críticos, um e-mail será enviado automaticamente! 📬

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
- Projeto desenvolvido como atividade de Aplicações Distrubuídas.
- [Vídeo com exemplo de uso]()