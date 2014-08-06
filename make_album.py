#!/usr/bin/python

import os, subprocess
from PIL import Image

# imagemagick command to make the orientation correct (my camera doesn't
# handle this correctly).  src and dest file can be the same
# convert -auto-orient src.jpg dest.jpg
#
# NOTE: this command is being called automatically in this script
# if it's available on the system path


# global settings
image_width = 600
album_title = "Album Name"

# supported image types only detected by lowercase extension
supported_types = ['jpg','jpeg','gif','png']

template = """
<html>
  <head>
    <title>{album_title}</title>
  </head>
  <body>

<style type="text/css">

body {{
  background-color: #999;
}}
a {{
  display: block;
  margin: 20px;
}}

img {{
  width: {image_width}px;
  max-width: 90%;
  display: block;
  margin: auto;
}}

</style>

  {photos_formatted}

  </body>
</html>
"""

# create thumbnail directory if it doesn't already exist
if not os.path.exists(".thumbnails"):
    os.makedirs(".thumbnails")

photo_html = """
    <a href="{image_filename}">
      <img src=".thumbnails/{image_filename}" alt="{image_filename}" />
    </a>
"""

photos_formatted = ""
for image_filename in os.listdir(os.getcwd()):
    image_extension = os.path.splitext(image_filename)[1].strip(".").lower()
    if image_extension in supported_types:
        try:
            result = subprocess.call(
                ['convert', '-auto-orient', image_filename, image_filename],
                stdout=open('/dev/null', 'wb'), stderr=subprocess.STDOUT
            )
        except OSError:
            # convert is not installed on this system
            pass
        image = Image.open(image_filename)
        # determining the ratio of width to height
        ratio = float(image.size[0]) / float(image.size[1])
        new_height = image_width / ratio
        image.thumbnail((image_width, image_width*3), Image.ANTIALIAS)
        image.save(".thumbnails/%s" % image_filename)
        photos_formatted += photo_html.format(image_filename=image_filename)

print template.format(album_title=album_title,
                      image_width=image_width,
                      photos_formatted=photos_formatted)

