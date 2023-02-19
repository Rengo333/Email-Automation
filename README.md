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

>name = 'YourAccount@hotmail.com'
>psswrd = 'YourPassword'

You can choose recipients by typing their emails on line 31
in square brackets and in quotation marks separated by a comma as follows:

> line 31 email_list = ["Your@Emails1.com", "Your@Emails2.com", "Your@Emails3.com"]

# Attachment
Attachment will be send together with every email.
It is up to you if you want to send a different file. 
It also needs to be in quotation marks as a string on line 48.

> f = "report.pdf"

# Log
Program creates a log file to save data about every email sent and every exception.