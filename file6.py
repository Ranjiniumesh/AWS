fruits=["Apple","Banana", "Mango"]
for fruit in fruits:
    print(fruit)

#using enumerate
for i, fruit in enumerate(fruits):
    print(i, fruit)

for i, fruit in enumerate(fruits):
    if fruit == "Banana":
        print(f"The {fruit} is found at index {i}")

#Lower & Upper cases
name=("Bangalore")
print(name.lower())
print(name.upper())

#Startswith function
if name.lower().startswith("ban"):
    print("true")
else:
    print("false")

if name.lower().endswith("roe"):
    print("true")
else:
    print("false")

#Replace
var="Good, Welcome to Devops, Evening"
print(var.replace('W', 'w'))
print(var.replace('Evening', 'Morning'))
print(var.replace(',', '/'))

#Split
print(var.split(','))
print(var.split(',', 1))
print(var.rsplit(',', 1))

mydict={"Name":"Ranjini", "Empid":"2699", "Company":"BEL"}
for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)

for key,value in mydict.items():
    print(f"{key} : {value}")
