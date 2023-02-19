import logging
import smtplib
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from schedule import every, run_pending

# Creating logger
logger = logging.getLogger(name="General")

# Setting logger to '.INFO' it will only log things that have a higher level than info.
logger.setLevel(level=logging.INFO)

# Creating filehandler to send the logs to email.log file
filer = logging.FileHandler("Email.log")

# adding handler to the logger
logger.addHandler(filer)

# This formats what information is added to the logger.
formatter = logging.Formatter('%(asctime)s:%(filename)s:%(funcName)s:%(levelname)s:%(message)s')

# adding this in order to link the formatter to the logger
filer.setFormatter(formatter)


def send_emails():
    # list of recipients, for safety purposes only examples are used here
    email_list = ["Your@Emails1.com", "Your@Emails2.com", "Your@Emails3.com"]

    # Connect to the Outlook.com SMTP server
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    try:
        name = 'YourAccount@hotmail.com'
        psswrd = 'YourPassword'
        # Login to the Hotmail account, for safety purposes use your own email created at https://signup.live.com/?lic=1
        server.login(name, psswrd)

        for i in email_list:
            try:
                logger.info(msg=f'Email sent to {i}', exc_info=True)
                # Compose the email message
                message = MIMEMultipart("Please see report attached.")
                message["Subject"] = "Test Email"
                message["From"] = name
                message["To"] = f'{i}'
                f = "report.pdf"
                # Create the attachment
                with open("report.pdf", "rb") as file:
                    # Add file as application/octet-stream
                    attachment = MIMEBase("application", "octet-stream")
                    attachment.set_payload(file.read())
                    # Encoding to ASCII so it can be sent across the network
                    encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition', 'attachment', filename=f)

                # Attach the attachment to the message
                message.attach(attachment)

                # Send the email
                server.send_message(message)

            except:

                # Writing to a log file
                logger.info(msg=f'unable to send email to {i}: ', exc_info=True)
    except:

        # Writing to a log file
        logger.info(msg=f'login failed: ', exc_info=True)

    # Disconnect from the server
    server.quit()


# scheduling to 8:00 am
every().day.at("08:00").do(send_emails)
# Loop so that the scheduling task keeps on running all time.
while True:
    # Checks whether a scheduled task is pending to run or not
    run_pending()
    time.sleep(1)
