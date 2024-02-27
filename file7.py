import sys
print(sys.argv)
print(f" The name is : {sys.argv[0]}")
print(f" Second index is : {sys.argv[0]}")

sys.exit(f"excecution is stopped forcefully")
print(f" Path is : (sys.path)")

import os
print(os.getcwd())
os.makedirs("dir1", exist_ok=True)
print(os.listdir("D:\pythonProject"))
