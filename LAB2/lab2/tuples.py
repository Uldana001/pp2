thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #allows dublicates

print(len(thistuple)) #5

thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry')

print(thistuple[1]) #banana
print(thistuple[-1]) #cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:]) #('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #Yes, 'apple' is in the fruits tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #('apple', 'kiwi', 'cherry')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) #('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) 
# This will raise an error because the tuple no longer exists
