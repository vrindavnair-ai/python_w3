fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits

print(green)
print(yellow)
print(red)

fruits = ["apple", "banana", "cherry"]

green, yellow, red = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 += tuple2
print(tuple1)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)