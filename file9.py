import sys
import os
for root,dirs_all,files in os.walk("/home/ubuntu"):
    #print(root,dirs_all,files)
    for file in files:
        if file.lower().startswith("notice") or file.lower().startswith("license"):
            os.chdir(root)
            with open(file, "r") as sr :
                content=sr.read()
                print(f"path of the file is :(root)\n displayed content of a file\n {content}")
            with open("/home/ubuntu/notice_license.txt","a") as sr:
                sr.write(f"{root}\n {content}")
