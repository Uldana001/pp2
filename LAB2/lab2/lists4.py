thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #['apple', 'banana', 'cherry']

mylist = list(thislist)
print(mylist) #['apple', 'banana', 'cherry']

mylist = thislist[:]
print(mylist) #['apple', 'banana', 'cherry']

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) #['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]