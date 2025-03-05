import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    name = input("Enter Name: ")
    if pattern.fullmatch(name):
        break
    else:
        print("Enter Name in correct format.")

while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    dob = input("Enter Date of Birth (DD-MM-YYYY):")
    if pattern.fullmatch(dob):
        break
    else:
        print("Enter DOB in correct format.")


while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    phone = input("Enter Mobile Number (XXX-XXX-XXXX): ")
    if pattern.fullmatch(phone):
        break
    else:
        print("Enter Mobile Number in correct format.")

while True:
    pattern = re.compile(r'^[a-zA-Z0-9]+@gmail\.com$')
    email = input("Enter Email: ")
    if pattern.fullmatch(email):
        break
    else:
        print("Enter Email in correct format.")


insta = input("Enter Insta ID: ")
print("\nAll details verified\n")


sender_email = "bhargavrayudu1502@gmail.com" 
sender_password = "gefl cvdr yfjb crlm"  

subject = "User Details"
body = f" Name: {name}\nDate of Birth: {dob}\nMobile: {phone}\nInstagram ID: {insta}\nEmail: {email}"


msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, email, msg.as_string())
server.quit()
print("Email sent successfully!")
