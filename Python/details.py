import os
pattren=["notice", "license"]
filename="notice_license.txt"
cur_dir=os.getcwd()
for pat in pattren:
    with open(filename, "a") as sr:
        sr.write(f"\n{pat}\n")
    for root, dir, files in os.walk(cur_dir):
        for file in files:
            if file.lower().startswith(pat):
                file_path=os.path.join(root, file)
                with open(file_path, 'r') as ni:
                    content = ni.read()
                with open(filename, 'a') as sh:
                    sh.write(f"{root}\n{content}")
    with open(filename, 'a') as fh:
        fh.write('#' * 50)
        fh.write("\n")
