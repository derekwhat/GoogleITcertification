"""
As part of the final course of the Google IT certification
Process directory of text files and upload to a running Web service
using requests
"""

import os
import requests

fields = "title name date feedback".split()
src = r"/data/feedback"
externalIP = r"35.232.92.252"
site = r"http://{}/feedback/".format(externalIP)
print(site)


def ProcessReviews(src, fields):
    files = os.listdir(src)
    reviews = []
    for file in files:
        # get content of review
        with open(os.path.join(src, file), 'r') as f:
            lines = [line.rstrip() for line in f.readlines()]

            # populate dictionary
            review = dict(zip(fields, lines))
            for field in fields:
                print("review {}: {}".format(fields[0], review[field]))
            reviews.append(review)
            f.close()
    print("--"*10)
    return reviews


def UploadReviews(dictOfReviews, site):
    for review in dictOfReviews:
        print(review)
        response = requests.post(site, data=review)
        print("status code: {}".format(response.status_code))
        response.raise_for_status()


UploadReviews(ProcessReviews(src, fields), site)


# if "__name__" == "__main__":
#     fields = "title name date feedback".split()
#     src = r"/data/feedback"
#     externalIP = r"35.232.92.252"
#     site = r"http://{}/feedback".format(externalIP)
#     UploadReviews(ProcessReviews(src, fields), site)

# student-01-5f8b2eead015@35.188.78.7
