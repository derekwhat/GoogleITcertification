""" helper for final assignment: Create and Send Email"""

# code is based on provided code from the week 3 assignment for the final course

import email
import mimetypes
import smtplib
import os


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # conditional added to accomodate when no pdf required to be sent
    # refer to heatlh_check.py
    if attachment_path != "":
        # Process the attachment and add it to the email
        attachment = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(), maintype=mime_type,
                                   subtype=mime_subtype, filename=attachment)
    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
