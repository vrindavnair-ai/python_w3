thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["brand"])

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  4 : 1964
}

print(thisdict)

x = thisdict.keys()
print(x)

y = thisdict.values()
print(y)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car.pop("model")
print(car)

car.popitem()
print(car)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

for x in thisdict:
  print(x)
  print(thisdict[x])

for c in thisdict.values():
  print(c)

for d in thisdict.keys():
  print(d)

for x, y in thisdict.items():
  print(x, y)

  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

for x, obj in myfamily.items():
  print(x,obj)

  for y in obj:
    print(y + ':', obj[y])