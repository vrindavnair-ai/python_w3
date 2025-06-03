def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(*kids):
  print("The youngest child is " + kids[2])
  print(kids)
  number = len(kids)
  print(number)

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])
  print(kid)

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(x, /): # only positional argument
  print(x)

my_function(3)

def my_function(*, x): #only keyword argument
  print(x)

my_function(x = 3)

def my_function(a, b, /, *, c, d): #a, b are positional only and c and d are keyword argument only.
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)