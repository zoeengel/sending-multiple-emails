from smtplib import SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)
senders_email = 'zengel1706@gmail.com'
receivers_emails = ['zengel1706@gmail.com', 'alexsassman65@gmail.com', 'adonisamber36@gmail.com','godwin@lifechoices.co.za']
password = input("Please enter password: \n")
# adding a subject
subject="Greetings"
msg=MIMEMultipart()
msg['From']=senders_email
msg['To']=", ".join(receivers_emails)
msg['Subject']=subject
# message to be sent
message = "Hi there ;-)\n"
message = message + "I hope this email finds you in good health during these trying times."

msg.attach(MIMEText(message, 'plain'))
text=msg.as_string()

# start TLS for security
s.starttls()
# Authentication
s.login(senders_email, password)
# sending the mail
s.sendmail(senders_email ,receivers_emails, text)
# terminating the session
s.quit()


