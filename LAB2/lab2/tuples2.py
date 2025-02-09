fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

"""
apple
banana
cherry
"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
"""
apple
banana
cherry
"""

for i in range(len(thistuple)):
  print(thistuple[i])
"""
apple
banana
cherry
"""

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
"""
apple
banana
cherry
"""

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')