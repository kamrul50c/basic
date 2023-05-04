import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'msaymon21@gmail.com'
sender_password = 'bnsamuwhqlktneki'
receiver_email = 'harashid@uttarauniversity.edu.bd'
subject = 'Sending an email using python code with an attachment '
body = 'dear Harun-Ar-Rashid sir \n\n  Take my salam  " assalamu-alikum " hope you are doing well .May Allah bless you with good health and happiness. \n here is the  attachment for sending mail using python code \n\n Warm regards,\n kamrul hasan'

# Create a multipart message and set headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Add body to email
message.attach(MIMEText(body, 'plain'))

# Open file in binary mode
filename = 'file.py'
with open(filename, 'rb') as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    'Content-Disposition',
    f'attachment; filename= {filename}',
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Try to log in and send the email
try:
    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()
