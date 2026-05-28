from email.message import EmailMessage
import smtplib
import ssl 
from getpass import getpass
import os 

EMAIL = os.getenv('EMAIL_REMITENTE')
PASSWORD = os.getenv('EMAIL_PASSWORD')
#Prueba
RECEIVER_EMAIL = "becarios@apeiroo.com"

def send_email(asunto, receiver_email, cuerpo_mensaje):
    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = EMAIL
    msg['To'] = receiver_email
    msg.set_content(cuerpo_mensaje)
    
    port = 465
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(
            smtp_server,
            port, 
            context=context,
            ) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def send_alert(vm_id, componente, valor):
    asunto = f"Alerta en la máquina virtual {vm_id}"
    cuerpo = f"El uso de {componente} en la máquina virtual ''{vm_id}'' ha superado el umbral determinado (estado actual: {valor}%) durante los últimos 5 minutos."
    send_email(asunto, RECEIVER_EMAIL, cuerpo)
