car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

"""
dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])
"""

##############################

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
"""
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020])
"""

##############################

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

"""
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 1964, 'red'])
"""

################################

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Yes, 'model' is one of the keys in the thisdict dictionary

#################################

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

################################

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict["color"] = "red"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

thisdict.update({"color": "blue"})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'blue'}

thisdict.pop("model")
print(thisdict) #{'brand': 'Ford', 'year': 2020, 'color': 'blue'}

thisdict.popitem()
print(thisdict) #{'brand': 'Ford', 'year': 2020}

del thisdict["year"]
print(thisdict) #{'brand': 'Ford'}

thisdict.clear()
print(thisdict) #{}


################################
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x) 
"""
brand
model
year
"""

for x in thisdict:
  print(thisdict[x])
"""
Ford
Mustang
1964
"""

for x in thisdict.values():
  print(x)
"""
Ford
Mustang
1964
"""

for x in thisdict.keys():
  print(x)
"""
brand
model
year
"""

for x, y in thisdict.items():
  print(x, y)
"""
brand Ford
model Mustang
year 1964
"""






