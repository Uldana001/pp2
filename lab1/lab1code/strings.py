print("hello")
print('hello') #they are same

"""
You can use quotes inside a string, 
as long as they don't match the quotes 
surrounding the string:
"""
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])  #e

for x in "banana":
  print(x)

"""
b
a
n
a
n
a
"""

a = "Hello, World!"
print(len(a)) #13

txt = "The best things in life are free!"
print("free" in txt) #True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") 
#Yes, 'free' is present.

txt = "The best things in life are free!"
print("expensive" not in txt)