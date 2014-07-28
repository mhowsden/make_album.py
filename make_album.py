#!/usr/bin/python

import os
from PIL import Image

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
  width: 600px;
  max-width: 90%;
  display: block;
  margin: auto;
}

</style>


""")

# create thumbnail directory if it doesn't already exist

for image_filename in os.listdir(os.getcwd()):
    if image_filename.find('jpg') >= 0:
        image = Image.open(image_filename)
        print image.size
        print ('<a href="%s"><img src="%s" alt="%s" /></a>'
               % (image_filename,image_filename,image_filename))

print ("</body></html>")
