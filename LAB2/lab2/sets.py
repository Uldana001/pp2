thisset = {"apple", "banana", "cherry"}
print(thisset) #{'banana', 'cherry', 'apple'}
#cant have dublicates

thisset = {"apple", "banana", "cherry", True, 1, 2} #can have different data types

print(thisset) #{True, 2, 'banana', 'apple', 'cherry'}
#true and 1 are considered as same
#false and 0 are considered as same

print(len(thisset)) #5
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'cherry', 'banana', 'apple'}

for x in thisset:
  print(x)
"""
cherry
banana
apple
"""

print("banana" in thisset) #true
print("banana" not in thisset) #false

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) #{'orange', 'apple', 'banana', 'cherry'}



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) #{'mango', 'pineapple', 'papaya', 'banana', 'apple', 'cherry'}




thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) #{'apple', 'cherry', 'orange', 'banana', 'kiwi'}

thisset.remove("banana")

print(thisset) #{'cherry', 'orange', 'apple', 'kiwi'}

thisset.discard("apple")

print(thisset) #{'cherry', 'orange', 'kiwi'}

x = thisset.pop()

print(x)

print(thisset)
"""
orange
{'kiwi', 'cherry'}
"""

thisset.clear()

print(thisset) #set()

#The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}



set3 = set1.union(set2)
print(set3) #{1, 2, 3, 'a', 'c', 'b'}



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) #{'b', 1, 2, 'a', 3, 'c'}




set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) #{1, 2, 3, 'bananas', 'c', 'a', 'apple', 'cherry', 'b', 'John', 'Elena'}

myset = set1 | set2 | set3 |set4
print(myset) #{1, 2, 3, 'cherry', 'Elena', 'apple', 'b', 'a', 'bananas', 'c', 'John'}

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) #{1, 'b', 2, 3, 'a', 'c'}

set1.update(set2)
print(set1) #{'b', 1, 2, 3, 'a', 'c'}




set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) #apple

set3 = set1 & set2
print(set3) #apple

set1.intersection_update(set2)

print(set1) #{'apple'}




set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3) #{False, 1, 'apple'}



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) #{'banana', 'cherry'}

set3 = set1 - set2
print(set3) #{'banana', 'cherry'}

set1.difference_update(set2)
print(set1) #{'banana', 'cherry'}

set3 = set1.symmetric_difference(set2)
print(set3) #{'banana', 'cherry', 'google', 'apple', 'microsoft'}

set3 = set1 ^ set2
print(set3) #{'banana', 'microsoft', 'cherry', 'apple', 'google'}

set1.symmetric_difference_update(set2)
print(set1) #{'banana', 'microsoft', 'apple', 'cherry', 'google'}


