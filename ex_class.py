class MyClass:
    x= 5;

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name #self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    self.age = age

  def __str__(self): #controls what should be returned when the class object is represented as a string.
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1)
p1.myfunc()


class Person:
  #self paramwtwer does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

class Student1(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) #to inherit properties from parent class. Else it will be override.
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

p2 = Student1("vri", "yad", 2013)
p2.welcome()


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers2:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers2()
myiter = iter(myclass)

for x in myiter:
  print(x)


#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


  #### with parent class vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car1(Vehicle):
  pass

class Boat1(Vehicle):
  def move(self):
    print("Sail!")

class Plane1(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car1("Ford", "Mustang")       #Create a Car object
boat1 = Boat1("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane1("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
