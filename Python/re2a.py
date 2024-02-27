import os
import re
name=["notice", "license"]
file="notice_license.txt"
with open (file, 'r') as sr:
    content=sr.read()
    for i in name:
        res=re.findall(i,content)
        print(res)
