import math
print("enter your name : ")
x = input()
print(f"Hi, {x}")

age = input("enter your age : ")
print(f"{x} is {age} years old")

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

y = True
while y == True:
  x = input("Enter a new number:")
  try:
    x = float(x)
    y = False
  except:
    print("Wrong input, please try again.")

  else:
    print("inside else")

  finally:
    print("inside finally")

print("Thank you!")