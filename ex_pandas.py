import pandas as pd
df = pd.read_csv("/Users/vrindavnair/Documents/Vrinda/learn/python_tutorial/insurance.csv")
#print(df)  #uncomment to see dataframe
#print("To string")   
#print(df.to_string()) 

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(pd.__version__)

a = [1,2,3]

var2 = pd.Series(a) #series is like column
print(var2)

print(var2[0])

myvar3 = pd.Series(a, index = ["x", "y", "z"])

print(myvar3)
print(myvar3["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar4 = pd.Series(calories)

print(myvar4)

myvar5 = pd.Series(mydataset)
print(myvar5)

print(myvar4["day1"])



myvar6 = pd.Series(calories, index = ["day1", "day2"])

print(myvar6)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
print(df.loc[0])
print(df.loc[[0,1]])

df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"]) #To have custom index

print(df2)

print(df2.loc["day2"])

df3 = pd.read_csv("data.csv")
print(df3)
print(pd.options.display.max_rows)

pd.options.display.max_rows = 60

print(df3)

df4 = pd.read_json("data.json")
print(df4)

#print(df4.to_string()) # to print entir dataframe

DATA2 = data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}    #json is same as python dictionary

df5 = pd.DataFrame(DATA2)
print(df5)

print(df3.head(10))

print(df3.tail(10))

print(df3.info())