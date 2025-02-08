x="awesome" #global variable

def myfunc():
    print("Python is " + x)
myfunc()
#Python is awesome

print("Python is " + x)
#Python is awesome

def myfunc():
    global x
    x="fantastic"

myfunc()
print("Python is "+ x)
#Python is fantastic

x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Python is fantastic