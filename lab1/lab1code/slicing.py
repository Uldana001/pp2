b = "Hello, World!"
print(b[2:5]) #llo
print(b[:5]) #Hello
print(b[2:]) #llo, World!
print(b[-5:-2]) #orl


print(b.upper()) #HELLO, WORLD!
print(b.lower()) #hello, world!

a = " Hello, World! "
print(a.strip()) #Hello, World!

print(b.replace("H", "J")) #Jello, World!
print(b.split(",")) #['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld

c = a + " " + b
print(c) #