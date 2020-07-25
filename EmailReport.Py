""" Part Four of final assignment: Email Process Updates"""

# code is based on earlier submitted ProcessData.py

import datetime
import os
from reports import generate_report
from emails import generate_email, send_email


def content(src):
    """Generate email containing name and weight of each image-description pair
    which was processed and uploaded in part 1, 2, 3 of final assignment"""
    names = []
    weights = []
    for item in os.listdir(src):
        filePath = os.path.join(src, item)
        with open(filePath, 'r') as f:
            line = f.readlines()
            weight = line[1].strip('\n')
            name = line[0].strip('\n')
            names.append("name: {}".format(name))
            weights.append("weight: {}".format(weight))

    paragraph = ""
    # create paragraph
    for i in range(len(names)):
        paragraph += "{}<br />{}<br /><br />".format(names[i], weights[i])
    return paragraph


if __name__ == "__main__":
    user = os.getenv('USER')
    src = '/home/{}/supplier-data/descriptions/'.format(user)
    # date format: "May 5, 2020"
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(str(current_date))
    pdfPath = '/tmp/processed.pdf'
    generate_report(pdfPath, title, content(src))

    recepient = "automation@example.com"
    sender = "{}@example.com".format(user)
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment = pdfPath
    msg = generate_email("automation@example.com", sender,
                         email_subject, email_body, attachment)
    send_email(msg)
