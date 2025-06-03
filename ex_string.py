a = "Hello, World!" # strings are arrays
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "hello"
print(b[1:3])
print(b[:3])
print(b[3:])

b = "Hello, World"
print(b[-5:-2])
print(b.upper())
print(b.lower())
c = " Hello, World  "
print(c)
print(c.strip())

print(b.replace("H", "J"))
print(b.split(","))
a = "vrinda"
b = "yadhu"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, I am " + str(age)
print(txt)

age = 36
txt = f"My name is {a}, I am {age},"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

print("hello \"vrinda\"")