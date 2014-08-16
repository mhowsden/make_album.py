#!/usr/bin/python

import os
from PIL import Image

# imagemagick command to make the orientation correct (my camera doesn't
# handle this correctly).  src and dest file can be the same
# convert -auto-orient src.jpg dest.jpg

# global settings
image_width = 1000
album_title = "Album Name"

print ("<html><head><title>%s</title></head><body>" % album_title)
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
  max-width: %spx;
  width: 100%%;
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
