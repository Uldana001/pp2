def count(s):
    u = sum(1 for char in s if char.isupper())
    l = sum(1 for char in s if char.islower())
    return u, l

text = "Hello World! Python is Fun"
upper, lower = count(text)
print(upper, lower)