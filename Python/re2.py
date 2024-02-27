import os
import re
pattern=["notice", "license"]
for pat in pattern:
    for root, dir, files in os.walk(os.getcwd()):
        for file in files:
            if file.lower().startswith(pat):
                with open ("/home/ubuntu/Python/notice_license.txt", 'r') as sh:
                    content= sh.read()
                    fetch=re.search(file, content)
                    print(fetch)
