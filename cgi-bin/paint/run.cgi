#!/usr/bin/env python3

import os
import random 
from urllib.parse import unquote
from PIL import Image, ImageDraw
from palette import pal

print("20 text/gemini",end="\r\n")

print("# Gemini Paint")

try:

  cmd=os.getenv("QUERY_STRING")

  cmdstr=""

  if cmd:

    cmd=unquote(cmd)

    cmds=cmd.split("\n")

    img = Image.open('/home/fria/gemini/cgi-bin/paint/painting.jpg').convert('RGB')

    draw = ImageDraw.Draw(img)


    for tok in cmds:
    
      toks=tok.split(" ")

      if toks[0]=="line" and len(toks)==7:

        draw.line((int(toks[1]),int(toks[2]),int(toks[3]),int(toks[4])), fill=pal[int(toks[5])], width=int(toks[6]))

        cmdstr+=f"line ({toks[1]}, {toks[2]},  {toks[3]}, {toks[4]}), fill=pal[{toks[5]}], width={toks[6]}\n"

      elif toks[0]=="oval" and len(toks)==8:
      
        draw.ellipse((int(toks[1]),int(toks[2]),int(toks[3]),int(toks[4])), fill=None if toks[5]=='none' else pal[int(toks[5])], outline=None if toks[6]=='none' else pal[int(toks[6])], width=int(toks[7]))

        cmdstr+=f"oval ({toks[1]}, {toks[2]}, {toks[3]}, {toks[4]}), fill=pal[{toks[5]}], outline=pal[{toks[6]}], width={toks[7]}\n"

      elif toks[0]=="rect" and len(toks)==8:

        draw.rectangle((int(toks[1]),int(toks[2]),int(toks[3]),int(toks[4])),fill=None if toks[5]=='none' else pal[int(toks[5])],outline=None if toks[6]=='none' else pal[int(toks[6])],width=int(toks[7]))

        cmdstr+=f"rect({toks[1]}, {toks[2]}, {toks[3]}, {toks[4]}), fill=pal[{toks[5]}], outline=pal[{toks[6]}], width={toks[7]};\n"

      elif toks[0]=="poly":

        pts=[]
        npts=len(toks)-3
        if npts>4:
          for i in range(1,npts,2):
            pts.append((int(toks[i]),int(toks[i+1])))

          draw.polygon(pts,fill=None if toks[npts+0]=='none' else pal[int(toks[npts+0])],outline=None if toks[npts+1]=='none' else pal[int(toks[npts+1])],width=int(toks[npts+2]))

          cmdstr+=f"poly {pts}, fill=pal[{toks[npts+0]}], outline=pal[{toks[npts+1]}], width={toks[npts+2]}\n"

      elif toks[0]=="arc" and len(toks)==8:

        draw.arc((int(toks[1]),int(toks[2]),int(toks[3]),int(toks[4])),start=int(toks[5]),end=int(toks[6]),fill=None if toks[7]=='none' else pal[int(toks[7])])

        cmdstr+=f"arc({toks[1]}, {toks[2]}, {toks[3]}, {toks[4]}), start={toks[5]}, end={toks[6]}, fill=pal[{toks[7]}]\n"

      elif toks[0]=="pie" and len(toks)==10:

        draw.pieslice((int(toks[1]),int(toks[2]),int(toks[3]),int(toks[4])),start=int(toks[5]),end=int(toks[6]),fill=None if toks[7]=='none' else pal[int(toks[7])],outline=None if toks[8]=='none' else pal[int(toks[8])],width=int(toks[9]))

        cmdstr+=f"pie({toks[1]}, {toks[2]}, {toks[3]}, {toks[4]}), start={toks[5]}, end={toks[6]}, fill=pal[{toks[7]}], outline=pal[{toks[8]}], width={toks[9]}\n"

      else:

        cmdstr+="Command Error\n"

    img.save("/home/fria/gemini/cgi-bin/paint/painting.jpg")

except:
  cmdstr+="Command Error"

print(cmdstr);

print("=> painting.jpg View")
print("=> input.cgi Draw")

print("""```Syntax

syntax:



line x0 y0 x1 y1 fill width

oval x0 y0 x1 y1 fill outline width

rect x0 y0 x1 y1 fill outline width

poly x0 y0 x1 y1 ... xn yn fill outline width

arc x0 y0 x1 y1 start end fill

pie x0 y0 x1 y1 start end fill outline width


fill = none or 0 to 15

outline = none or 0 to 15

width = integer
  
```""")

print("=> palette.png Color Palette")
