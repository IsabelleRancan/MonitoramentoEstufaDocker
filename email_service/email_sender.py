import smtplib
from email.message import EmailMessage
import os

EMAIL_REMETENTE = os.environ.get("EMAIL_REMETENTE")
SENHA_APP = os.environ.get("SENHA_APP")
EMAIL_DESTINO = os.environ.get("EMAIL_DESTINO")

def enviar_email(dados):
    estufa_id = dados.get("id")
    temperatura = dados.get("temperatura")
    sensacao = dados.get("sensacao_termica")
    umidade = dados.get("umidade")

    assunto = f"⚠️ ALERTA CRÍTICO: Estufa #{estufa_id}"
    corpo = f"""
    🚨 Monitoramento Crítico da Estufa #{estufa_id} 🚨

    🔥 Temperatura: {temperatura}°C
    🥵 Sensação Térmica: {sensacao}°C
    💧 Umidade: {umidade}%

    Verifique imediatamente as condições da estufa!
    """

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINO
    msg.set_content(corpo)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA_APP)
            smtp.send_message(msg)
        print("✅ E-mail real enviado com sucesso!")
    except Exception as e:
        print("❌ Erro ao enviar e-mail:", e)
