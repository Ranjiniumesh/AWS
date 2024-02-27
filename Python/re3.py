import re
email_data="ranjini <ranjini@gmail.com>, shiva <shiva@gmail.com>, shivani <shivani@gmail.com>, ranjitha01 <ranjitha01@gmail.com>, Ranjini <Ranjini@gmail.com>, ranjini07 <ranjini07@gmail.com>"
result=re.search("ra[n, z]", email_data)
print(result)

result=re.search("ranji[n, t]", email_data)
print(result)

result=re.search("ranji[n, z]+", email_data)
print(result)

result=re.search("ranji[a, z]+", email_data)
print(result)

result=re.findall("ranji[n, t]", email_data)
print(result)

result=re.findall("ranji[n, z]+", email_data)
print(result)

result=re.search("ranji[n, z]+", email_data, re.IGNORECASE)
print(result)

result=re.findall("ranji[n, t]+", email_data, re.IGNORECASE)
print(result)

result=re.search("ranji[n, t]+[0-9]+", email_data, re.IGNORECASE)
print(result)

result=re.findall("ranjin[i, z]+[0-9]+", email_data)
print(result)

result=re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+", email_data)
print(result)

result=re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+", email_data)
print(result)

result=re.findall(r"\w+@\w+\.\w+", email_data)
print(result)
