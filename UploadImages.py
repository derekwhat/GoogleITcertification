""" Part Two of final assignment, upload pictures"""

# code is based on earlier submitted TextToWebService.py

import os
import requests

user = os.getenv('USER')
src = '/home/{}/supplier-data/images/'.format(user)
dest = "http://localhost/upload/"

files = os.listdir(src)
# Parsing through all the images
for file in files:
    # Accepting jpeg files and ignore others
    if not ('jpeg' in file and file.startswith('.')):
        fullPath = os.path.join(src, file)
        with open(fullPath, 'rb') as f:
            r = requests.post(dest, files={'file': f})
