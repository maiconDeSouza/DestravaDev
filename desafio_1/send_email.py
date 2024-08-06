import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
username = os.getenv("USER_NAME_EMAIL")
password = os.getenv("PASSWORD_EMAIL")

from_email = username
to_email = os.getenv("TO_EMAIL")
subject = 'Previsão do Tempo'

def send_email(body):
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))
    
    smtp_server_instance = None

    try:
        print("Connecting to SMTP server...")
        smtp_server_instance = smtplib.SMTP(smtp_server, smtp_port, timeout=30)
        smtp_server_instance.set_debuglevel(1)
        smtp_server_instance.starttls()
        print("Starting TLS session...")
        smtp_server_instance.login(username, password)
        print("Login successful!")
        smtp_server_instance.sendmail(from_email, to_email, message.as_string())
        print('Email sent successfully!')
    except smtplib.SMTPAuthenticationError as e:
        print(f'SMTP Authentication Error: {e.smtp_code} - {e.smtp_error}')
    except smtplib.SMTPConnectError as e:
        print(f'SMTP Connection Error: {e}')
    except smtplib.SMTPException as e:
        print(f'SMTP General Error: {e}')
    except Exception as e:
        print(f'Error sending email: {e}')
    finally:
        if smtp_server_instance:
            try:
                smtp_server_instance.quit()
                print("Connection closed.")
            except Exception as e:
                print(f'Error closing connection: {e}')
