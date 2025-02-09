thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print(thisdict["brand"]) #Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #cant have dublicates
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

print(len(thisdict)) #3
print(type(thisdict)) #<class 'dict'>




thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) #{'name': 'John', 'age': 36, 'country': 'Norway'}






