names = ["Apple", "Orange", "Banana"]
val = "Mango"
if val in names:
    print("the name is in the list")
else:
    print("the names is not in list")

mydict = {"Name":["Shiva", "Ranjini"], "Place":["Bangalore", "Mysore"], "Company":["BEL", {"MPPL":["Engineer", "Manager"]}]}
if "Company" in mydict and "Manager" in mydict["Company"][1]["MPPL"]:
        print("The value is present")
else:
        print("The value is not present")

mydict1 = {}
if mydict1:
    print("mydict1 is not empty")
else:
    print("mydict1 is empty")
if not mydict1:
    print("mydict1 is empty")
else:
    print("mydict1 is not empty")

mydict2 = {10, 20}
if mydict2:
    print("mydict2 is not empty")
else:
    print("mydict2 is empty")
if not mydict2:
    print("mydict2 is empty")
else:
    print("mydict2 is not empty")

flag=False
if flag:
    print("flag is true")
else:
    print("flag is false")
