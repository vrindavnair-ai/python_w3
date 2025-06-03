x = "awesome"
a = "global"
def myfunc():
    print("Python is " + x)

def myfunc_2():
    x = "fantastic"
    print("Python is " + x)


def myfunc_3():
    y = "amazing"
    print("Python is " + y)

def myfunc_4():
    global z 
    z = "great"
    print("Python is " + z)

def myfunc_5():
    global a 
    a = "local"
    print("global variable changed inside function")

myfunc()
myfunc_2()
myfunc_3()
myfunc_4()
print(x)
#print(y) not defined as it is local variable
print(z)
print(a)
myfunc_5()
print(a)