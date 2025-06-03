x = lambda a : a + 10
print(x(5))

#can have any number arguments but can have only one expression
x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

mytripler = myfunc(3)

print(mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time