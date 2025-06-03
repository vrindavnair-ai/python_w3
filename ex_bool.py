print(bool("abc"))
bool(123)
bool(["apple", "cherry", "banana"])

print(bool(False))
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print(10<5)

class myclass():
  def __len__(self): #only__len__ function
    return 0  # return False

myobj = myclass()
print(bool(myobj))