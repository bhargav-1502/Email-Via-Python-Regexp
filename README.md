# Email-Via-Python-Regexp

# Overview
This Python script demonstrates how to validate user input using regular expressions (regex) and send an email with the collected details. The script ensures that the user provides valid information for their name, date of birth, mobile number, and email address. Once validated, the details are sent to the provided email address using the smtplib library.

# Features

•  Validates user inputs:
    •   Name (Only letters and spaces)

    •   Date of Birth (Format: DD-MM-YYYY)

    •   Mobile Number (Format: XXX-XXX-XXXX)
    
    •   Email (Only Gmail addresses)
    
    •   Collects Instagram ID as additional information.

    •   Sends the collected details to the provided email using Gmail's SMTP server.

 # Prerequisites

  •  Python 3.x

  •  An active Gmail account with "Less secure apps" access enabled (or an app password).

      
 # Installation
 
   1. Clone this repository:
      
        git clone https://github.com/yourusername/your-repository.git
        cd your-repository

   2. Install the required dependencies (if not already installed):

        pip install smtplib email

  # Usage

    1. Run the script

         python Email\ via\ Python\(regexp\).py

    2. Enter the required details when prompted.
    
    3. The script will validate the inputs and send an email with the details.     


 # Configuration

   . Modify sender_email and sender_password in the script to match your Gmail credentials.

   . For security reasons, consider using an app password instead of your actual Gmail password.

   
