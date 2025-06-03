import pandas as pd
import matplotlib.pyplot as plt
import time
import matplotlib
import sys
matplotlib.use('Agg') #for hostogram
matplotlib.use('TkAgg') #otherwise it won't show plot with plt.show(block=False)
df  = pd.read_csv("data4.csv")
df2 = pd.read_csv("data4.csv")
df3 = pd.read_csv("data4.csv")
print(df.to_string)

new_df = df.dropna() #creating a new data frame without null values
print(new_df.to_string())

#df.dropna(inplace=True) #remove all rows containing NULL values from the original DataFrame.

print(df)

df.fillna(130, inplace=True) #Replace all null values with value 130

print(df)

df2.fillna({"Calories":130}, inplace=True) #Filing only a specified column

print(df2)

x= df3["Calories"].mean() #finding mean
y=df3["Calories"].median()#finding median if you want to replace it with median
z=df3["Calories"].mode()[0] #Finding mode if you want to replace it with mode, if there are multiple value [0] helps in extracting 1 value
print("mean",x)
print("Median",y)
print("Mode",z)
df3.fillna({"Calories":x}, inplace=True) #replacing with mean value
print(df3)

df3['Date'] = pd.to_datetime(df['Date'],format='mixed') # To change every date column in date format
print(df3)

df2.dropna(subset=['Date'], inplace = True) #to remove null values in data
print(df2)
df2['Date'] = pd.to_datetime(df['Date'],format='mixed')
print(df2)

df2.loc[7, 'Duration'] = 45 #Replacing value at 7th row to 45

print(df2)

for x in df3.index: #setting a rule for large dataset
    if df3.loc[x,"Duration"]>120: 
        df3.loc[x,"Duration"] = 120

print(df3)

for x in df3.index:
  if df3.loc[x, "Duration"] > 110: 
    df3.drop(x, inplace = True) #To remove values which is out of range

print(df3)

print(df3.duplicated()) #To check if any row is duplicate. Returns True if it is duplicate.
df3.drop_duplicates(inplace=True) #To drop duplicates ,(inplace = True) will make sure that the method does NOT return a new DataFrame
print(df3)

print(df3.corr())#The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

df5 = pd.read_csv('data5.csv')
print(df5)
df5.plot()

plt.show(block=False)
time.sleep(5)
plt.close()
df5.plot(kind = 'scatter', x = 'Pulse', y = 'Calories') #drawing columns with high correlation

plt.show(block=False)
time.sleep(5)
plt.close()

df5["Duration"].plot(kind='hist')  # ✅ Correct function call with parentheses

plt.title("Histogram of Duration")
plt.show(block=False)              # ✅ Show the plot without blocking
time.sleep(10)                      # ✅ Wait 5 seconds
 