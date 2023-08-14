#!/usr/bin/env python3

import os

cmd=os.getenv("QUERY_STRING")
if not cmd: 
    print("10 Command:",end="\r\n")
    quit()

print("30 run.cgi?"+cmd,end='\r\n')
