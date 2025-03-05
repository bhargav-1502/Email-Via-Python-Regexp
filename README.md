# Email-Via-Python-Regexp

# Overview
This Python script demonstrates how to validate user input using regular expressions (regex) and send an email with the collected details. The script ensures that the user provides valid information for their name, date of birth, mobile number, and email address. Once validated, the details are sent to the provided email address using the smtplib library.

# Features

• Input Validation:

    • Name: Only alphabets and spaces are allowed.
   
    • Date of Birth: Must be in the format DD-MM-YYYY.

    • Mobile Number: Must be in the format XXX-XXX-XXXX.

    • Email: Must be a valid Gmail address (e.g., example@gmail.com).

• Email Sending:

   • Collects user details and sends them via email using Gmail's SMTP server.

   • Uses the smtplib library to send the email.

 # Prerequisites
 Ensure you have the following installed:

  •  Python 3.x

  •  Required Python libraries:

      pip install smtplib email

 # How to Use
   1. Clone this repository:

         git clone https://github.com/your-username/repository-name.git

   2. Navigate to the project directory:

         cd repository-name

   3. cd repository-name

         python Email_via_Python.py

   4. Follow the on-screen prompts to enter your details.

   5. The script will validate your inputs and send an email with the provided details.

 # Configuration

 Modify the following lines in the script to use your own Gmail credentials:

  sender_email = "your-email@gmail.com"
  sender_password = "your-app-password"

  Note: For security reasons, use an App Password instead of your main Gmail password.
