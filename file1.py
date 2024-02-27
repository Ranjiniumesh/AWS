var ="good evening"
count=len(var)
print (count)
print(f"The lenght of the string {count}")
print(var[0], var[1])
print(var[0:6])

#Reversing indexing
print(var[-1], var[-4])

#List
mylist=[]
print(f"{mylist}")
mylist=[10, 20, 30]
print(mylist)
print(mylist[0], mylist[1], mylist[2])

#String List
mylist2=["Welcome", "to", "devops"]
print(mylist2[0], mylist2[1], mylist2[2])
count1=len(mylist2)
print(f"Length of list is {count1}")

# appending new list

mylist2.append("devops")
print(mylist2)

mylist2.append("welcome")
mylist2.append(56)
print(mylist2)

#To delete element
mylist2.pop()
print(mylist2)
mylist2.pop(0)
print(mylist2)

#To replace element
mylist2[3]="python"
print(mylist2)

#To append one list to another
mylist3=["welcome", "goodevening"]
mylist2.extend(mylist3)
print(mylist2)
