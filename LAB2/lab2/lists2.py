thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist #delete the entire list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #clear the list content

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""
apple
banana
cherry
"""

for i in range(len(thislist)):
  print(thislist[i])

"""
apple
banana
cherry
"""

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
"""
apple
banana
cherry
"""

[print(x) for x in thislist]
"""
apple
banana
cherry
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #['apple', 'banana', 'mango']

newlist = [x for x in fruits if "a" in x]

print(newlist) #['apple', 'banana', 'mango']

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]