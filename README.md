# Email Automation

This program was created to automatically send emails every day at a certain time
with an attachment called report.pdf.
Time is defined at line 78. It is up to you what time you choose. 
Time needs to be in quotation marks as a string. Use 24 hour format.

> line 78 every().day.at("08:00").do(send_emails)

# Email server

Program uses SMTP outlook server to send emails.
You need to create an email account [here](https://signup.live.com/?lic=1).

# Email account and recipients

Type your email and password on line 37 and 38 in quotation marks as a string as follows: 

>line 37 name = 'YourAccount@hotmail.com'
>line 38 psswrd = 'YourPassword'

You can choose recipients by typing their emails on line 31
in square brackets and in quotation marks separated by a comma as follows:

> line 31 email_list = ["Your@Emails1.com", "Your@Emails2.com", "Your@Emails3.com"]

# Email message

If you want to change the subject you can do so on lines 46-47
the same way you did with email and password.

> line 46 message = MIMEMultipart("Please see report attached.")
> line 47 message["Subject"] = "Test Email"

# Attachment

Attachment will be send together with every email.
It is up to you if you want to send a different file. 
It also needs to be in quotation marks as a string on line 48.

> f = "report.pdf"

# Log
Program creates a log file to save data about every email sent and every exception.

# Requirements
Additional libraries are required to install.
It is recommended to use a new virtual envinronment.
Use this command in terminal to install requirements from requirements.txt.
>pip install -r requirements.txt