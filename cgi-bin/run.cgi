#!/usr/bin/env python3

import os
import random 
from urllib.parse import unquote
from PIL import Image, ImageDraw

pal=[
  (26,28,44),
  (93,39,93),
  (177,62,83),
  (239,125,87),
  (255,205,117),
  (167,240,112),
  (56,183,100),
  (37,113,121),
  (41,54,111),
  (59,93,201),
  (65,166,246),
  (115,239,247),
  (244,244,244),
  (148,176,194),
  (86,108,134),
  (51,60,87),
]



cmd=os.getenv("QUERY_STRING")

if cmd:

  cmd=unquote(cmd)

  cmds=cmd.split("\n")

  img = Image.open('images/painting.jpg').convert('RGBA')

  img = Image.new('RGBA', img.size, (255,255,255,0))
  draw = ImageDraw.Draw(img)

  for tok in cmds:
    toks=tok.split(" ")

    if toks[0]=="line" and toks.length==7:

      draw.line((toks[1],toks[2],toks[3],toks[4]), fill=pal[toks[5]],width=toks[6])

    elif toks[0]=="oval" and tok.length==6:
    
      draw.ellipse((toks[1],toks[2]), fill=pal[toks[3]], outline=pal[toks[4]], width=toks[5],)

    elif toks[0]=="rect" and tok.length==8:

      draw.rectangle((toks[1],toks[2],toks[3],toks[4]),fill=pal[toks[5]],outline=pal[toks[6]],width=toks[7])

    elif toks[0]=="poly":

      pts=[]
      siz=len(toks)-4
      if size>4:
        for i in range(1,siz,2):
          pts.append(toks[i],toks[i+1])

        draw.polygon(pts,fill=pal[toks[siz+0]],outline=pal[toks[siz+1]],width=toks[siz+2])



print("20 text/gemini",end="\r\n")

print("=> painting.png painting")
print("=> input.cgi Input Command")
