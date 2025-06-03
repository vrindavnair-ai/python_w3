try:
  print(x)
except:
  print("An exception occurred")


try:
  print(x)

except NameError:
  print("Variable x is not defined")

except:
  print("An exception occurred")


try:
  print("Hello")
except:
  print("Something went wrong")
else: #executed if no errors are there
  print("Nothing went wrong")

#x=5

try:
  print(x)
except:
  print("Something went wrong")
finally: #Excecuted regardless of the output of try except
  print("The 'try except' is finished")


x = 1

if x < 0:
  raise Exception("Sorry, no numbers below zero") #raise keyword is used to raise an exception. and stop the program

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")