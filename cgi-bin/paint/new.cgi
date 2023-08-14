#!/usr/bin/env python3

#!/usr/bin/env python3

import PIL
from PIL import Image, ImageDraw
from palette import pal

img = PIL.Image.new(mode="RGB", size=(256, 256), color=pal[12])

img.save("/home/fria/gemini/cgi-bin/paint/painting.jpg")
 
print("20 text/gemini",end="\r\n")

print("New Image Created")

print("=> run.cgi Draw")
