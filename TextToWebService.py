"""
As part of the final course of the Google IT certification
Process directory of text files and upload to a running Web service
using requests
"""

import os
import requests

fields = "title name date feedback".split()
src = r"/data/feedback"

def ProcessReviews(src):
    files = os.listdir(src)
    reviews = []
    for file in files:
        #get content of review
        with open(file, 'r') as f:
            f.readlines()

            #populate dictionary
            review = {field: line for line in f for field in fields}
            print("review: {}".format(review))
            reviews.append(review)

    #return a list of dictionaries of parsed reviews
    #

def UploadReviews(dictOfReviews, site):
    for review in dictOfReviews:
        # convert to Json??

        response = requests.post(site, data=review)
