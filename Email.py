import smtplib
import ssl
from email.message import EmailMessage
from Pass import password  


email_sender = "sandipkda@gmail.com"
email_password = password
email_receiver= "" #enter the email of the receiver here.
subject ="This is a test Automation email."
body =" Hello, This is my first shot at sending emails with python as well as learning python."

em=EmailMessage()
em['From']= email_sender
em['To']=email_receiver
em['Subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())