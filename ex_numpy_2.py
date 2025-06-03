import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

y = arr.view()
arr[1] = 52
print(arr)
print(y)
y[3] = 62
print(arr)
print(y)
print(arr.base)
print(x.base)
print(y.base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)
newarr2 = arr.reshape(2,3,2)
print(newarr2)
print(newarr2.base)
print(arr.reshape(2,2,-1)) #-1 if you want the numpy to calculate the third number based on the number of digits

newarr3 = newarr.reshape(-1)
print(newarr3) #to flatten array

for x in arr:
    print (x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
    for z in y:
      print(z)

print("Using nditer")
for x in np.nditer(arr):
  print(x)

print("ndenumerate")
for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)



print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

arr = np.concatenate((arr1, arr2))

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


newarr = np.array_split(arr, 2)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


import numpy as np

arr = np.array([10, 1, 2, 3, 4, 5, 4, 0, 4])

x = np.where(arr == 4) #finding indexes of value 4

print(x)

x = np.where(arr%2 == 1) #to find indexes of odd value

print(x)

arr_s = np.sort(arr)
print(arr_s)


arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False] #X is a filter - A boolean index list is a list of booleans corresponding to indexes in the array.

newarr = arr[x]

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)