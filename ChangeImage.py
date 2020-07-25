""" Part One of final assignment, reformat pictures"""

#!/usr/bin/env python3

import os
from PIL import Image

user = os.getenv('USER')
src = r'/home/{}/supplier-data/images/'.format(user)
for file in os.listdir(src):
    if not file.startswith('.') and 'tiff' in file:
        image_path = os.path.join(src, file)
        path = os.path.splitext(image_path)[0]
        im = Image.open(image_path)
        new_path = '{}.jpeg'.format(path)
        im.convert('RGB').resize((600, 400)).save(new_path, "jpeg")
