import os
import sys
#v = os.path.join("/home/ubuntu", "pytestdir")
#print(v)

#print(os.path.basename("/home/ubuntu/file8.py"))
for root, dir, files in os.walk("/home/ubuntu"):
    print(f"directory name: {os.path.basename(root)}")
    for file in files:
        if file.lower().endswith(".py"):
            print(file)
