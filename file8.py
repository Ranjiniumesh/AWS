import os
print(os.getcwd())

os.makedirs("pytestdir", exist_ok=True)
print(os.listdir("/home/ubuntu"))

os.chdir("pytestdir")
print(os.getcwd())

print (os.path.isfile("file4.py"))
print(os.path.exists("pytestdir"))
