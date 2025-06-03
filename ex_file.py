import os
with open ("demofile.txt", "w") as f:
  f.write("""Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!""")
  
f = open("demofile.txt", "r")
print(f.read())
f.close()

with open("demofile.txt", "r") as f:
  print(f.readlines())


with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

with open("demofile.txt", "r") as f:
  for x in f:
    print(x)

try:
    with open("demofile2.txt","x"):
     pass

except:
  print("file already exist")
#wait(5)
if os.path.exists("demofile3.txt"):
  os.remove("demofile3.txt")
else:
  print("The file does not exist")
#os.rmdir("ex_test")
if os.path.exists("/Users/vrindavnair/Documents/Vrinda/learn/python_tutorial/ex_test"):
  os.rmdir("/Users/vrindavnair/Documents/Vrinda/learn/python_tutorial/ex_test") #can be removed only if it is empty
  print("The folder has been deleted")
else:
  print("The folder does not exist")

  