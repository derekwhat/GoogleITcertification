""" Part Three of final assignment: Upload Image Descriptions"""

# code is based on earlier submitted TextToWebService.py

import os
import requests


def catalog_data(src, dest):
    """upload descriptions to accompany uploaded images via dictionaries
    """

    for item in os.listdir(src):
        fruit = {}
        filename = os.path.join(src, item)
        with open(filename, "r") as f:
            line = f.readlines()
            description = ""
            for i in range(2, len(line)):
                description += line[i].strip("\n").replace(r"\xa0", "")
                fruit["description"] = description
                fruit["weight"] = int(line[1].strip("\n").strip("lbs"))
                fruit["name"] = line[0].strip("\n")
                fruit["image_name"] = item.replace(".txt", ".jpeg")
                response = requests.post(dest, json=fruit)
                print(response.request.url)
                print(response.status_code)
    return 0


if __name__ == "__main__":
    dest = "http://localhost/fruits/"
    user = os.getenv("USER")
    src = "/home/{}/supplier-data/descriptions/".format(user)
    catalog_data(src, dest)
