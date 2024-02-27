var={}
print(var)
mydict={"devops": "python", "fruits": "orange"}
print(mydict)
print(mydict["fruits"])
print(mydict["devops"])

mydict={"devops": "python", "fruits": "orange", "name":["Aaa", "Bbb", "Ccc"]}
print(mydict)
print(mydict["name"])
print(mydict["name"][1])

mydict={"devops": "python", "fruits": "orange", "name":["Aaa", "Bbb", "Ccc"], "details": {"Company": "Brigade", "Location": "Bangalore"}}
print(mydict)
print(mydict["details"])
print(mydict["details"]["Location"])

mydict={"devops": "python", "fruits": "orange", "name":["Aaa", "Bbb", "Ccc"], "details": {"Company": "Brigade", "Location": ["Bangalore", "Chennai"]}}
print(mydict)
print(mydict["details"]["Location"][0])
