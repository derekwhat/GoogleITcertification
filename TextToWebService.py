"""
As part of the final course of the Google IT certification
Process directory of text files and upload to a running Web service
using requests
"""

import os
import requests

# fields = "title name date feedback".split()
# src = r"/data/feedback"
# site = r"http://<corpweb-external-IP>/feedback"


def ProcessReviews(src, fields):
    files = os.listdir(src)
    reviews = []
    for file in files:
        #get content of review
        with open(file, 'r') as f:
            lines = [line.rstip() for line in f.readlines()]

            # populate dictionary
            review = {field: line for line in lines for field in fields}
            print("review: {}".format(review))
            reviews.append(review)
            f.close()
    return reviews


def UploadReviews(dictOfReviews, site):
    for review in dictOfReviews:
        # convert to Json??

        response = requests.post(site, data=review)
        response.raise_for_status()


if "__name__" == "__main__":
    fields = "title name date feedback".split()
    src = r"/data/feedback"
    site = r"http://<corpweb-external-IP>/feedback"
    UploadReviews(ProcessReviews(src, fields), site)
