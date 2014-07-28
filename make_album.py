#!/usr/bin/python

import os
from PIL import Image

# global settings
image_width = 600


print ("<html><body>")
print ("""
<style type="text/css">
body {
  background-color: #999;
}
a {
  display: block;
  margin: 20px;
}

img {
  width: %spx;
  max-width: 90%%;
  display: block;
  margin: auto;
}

</style>


""" % image_width)

# create thumbnail directory if it doesn't already exist
if not os.path.exists(".thumbnails"):
    os.makedirs(".thumbnails")

for image_filename in os.listdir(os.getcwd()):
    if image_filename.find('jpg') >= 0:
        image = Image.open(image_filename)
        # determining the ratio of width to height
        ratio = float(image.size[0]) / float(image.size[1])
        new_height = image_width / ratio
        image.thumbnail((image_width,image_width*3),Image.ANTIALIAS)
        image.save(".thumbnails/%s" % image_filename)
        print ('<a href="%s"><img src=".thumbnails/%s" alt="%s" /></a>'
               % (image_filename,image_filename,image_filename))

print ("</body></html>")
