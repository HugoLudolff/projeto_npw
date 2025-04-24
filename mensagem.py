import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

host ="smtp.gmail.com"    
port = "587"
login = ""
senha = ""

def alerta(device):
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)

        corpo = f"O dispositivo {device} está offline"
        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = login
        email_msg['Subject'] = "Alerta de Dispositivo Offline"
        email_msg.attach(MIMEText(corpo, 'plain'))
        try:
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        except Exception as e:
            print(f"Erro ao enviar o email: {e}")
        print("Email enviado com sucesso!") 
    finally:
        server.quit()
