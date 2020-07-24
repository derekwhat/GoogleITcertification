"""
As part of the final course of the Google IT certification
Scale and convert images using PIL
"""
from PIL import Image
import os

path = r"/images"
dest = r"/opt/icons/"
print("running file now")
fileformat = ".jpeg"


def fixImage(folder, dest, fileformat):
    """changes all images within a folder of images, no subdirectories"""
    images = []
    for dirpath, __, files in os.walk(folder):
        # build out the full path to the image
        print(dirpath)
        print(files)
        print("------")
        print("image count: {}".format(len(images)))
        images = [[os.path.join(folder, f), f] for f in files]
    for file in images:
        # check properties of image
        img = Image.open(file[0])
        print("source: {}".format(file[0]))
        print("file format: {}  file size: {}".format(img.format, img.size))
        # change properties of image
        name = file[1]
        dest_path = os.path.join(dest, name)
        print("destination: {}".format(dest_path))
        (img.rotate(270)
            .resize((720, 720))
            .convert('RGB')
            .save(dest_path, fileformat))


fixImage(path, dest, fileformat)
## not sure why this did not work
if "__name__" == "__main__":
    path = r"/images"
    dest = r"/opt/icons/"
    fileformat = ".jpeg"
    print("running file now")
    fixImage(path, dest, fileformat)
