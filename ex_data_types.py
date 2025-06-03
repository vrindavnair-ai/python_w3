x = 5
print(x, type(x))
a = str("hello")
b= int(20)
c=float(20.5)   
d=complex(1j)
e = list(("apple", "banana", "cherry"))
f = tuple(("apple", "banana", "cherry"))
g = range(6)
h = dict(name="John", age=36)
h = set(("apple", "banana", "cherry"))
i = frozenset(("apple", "banana", "cherry"))
j = bool(5)
k = bytes(5)
l = bytearray(5)
m = memoryview(bytes(5))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))