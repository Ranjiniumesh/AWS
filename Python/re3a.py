import re
def find_pattern(pattern,data):
    result=re.findall(rf"{pattern}", data)
    return result

pat="ranji[n, t]"
email_data="ranjini <ranjini@gmail.com>, shiva <shiva@gmail.com>, shivani <shivani@gmail.com>, ranjitha01 <ranjitha01@gmail.com>"

res=find_pattern(pat, email_data)
print(res)

pat1="[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+"
email_data="ranjini <ranjini@gmail.com>, shiva <shiva@gmail.com>, shivani <shivani@gmail.com>, ranjitha01 <ranjitha01@gmail.com>"

res1=find_pattern(pat1, email_data)
print(res1)

pat2="ranji[n, t]+[0-9]+"
email_data="ranjin070 <ranjini@gmail.com>, shiva <shiva@gmail.com>, shivani <shivani@gmail.com>, ranjit01 <ranjitha01@gmail.com>"

res2=find_pattern(pat2, email_data)
print(res2)

pat3="\w+@\w+\.\w+"
email_data="ranjini <ranjini@gmail.com>, shiva <shiva@gmail.com>, shivani <shivani@gmail.com>, ranjitha01 <ranjitha01@gmail.com>"

res3=find_pattern(pat3, email_data)
print(res3)
