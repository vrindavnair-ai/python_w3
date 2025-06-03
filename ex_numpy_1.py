import numpy as np
arr = np.array([1 , 2, 3, 4 , 5])
print(arr)
print(arr.ndim)
print(type(arr))
print(np.__version__)
print(arr[0])
print("Slice is 1", arr[1:4])
print("Slice is 2", arr[:4])
print("Slice is 3", arr[1:])
print("Slice is 4", arr[-3:-1])
print("Slice is 5", arr[1::2]) # step 2
print("shape : ", arr.shape)

arr2 = np.array((1 , 2, 3, 4 , 5))  # 1-D array
print(arr2)
print(arr2.ndim)
print(type(arr2))

arr3 = np.array(42) # 0-D array
print(arr3)
print(arr3.ndim)

arr4 = np.array([[1,2,3,],[5,6,7]])
print(arr4)
print(arr4.ndim)
print(arr4[1, 1])
print("slice is ", arr4[1, 1:2])
print("shape : ", arr4.shape)

arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr5)
print(arr5.ndim)
print(arr5[1, 0, 2])
print(arr5[-1, -1, -1])
print("shape : ", arr5.shape)

arr6 = np.array([1, 2, 3, 4], ndmin=5)
print(arr6 )
print(arr6.ndim)
print("shape : ", arr6.shape)
"""In this array the innermost dimension (5th dim) has 4 elements, "
"the 4th dim has 1 element that is the vector, the 3rd dim has 1 element "
"that is the matrix with the vector, the 2nd dim has 1 element that is 3D array "
"and 1st dim has 1 element that is a 4D array."""

arr = np.array([[1, 2, 3,4,5], [6, 7, 8,9,10]])
print(arr.ndim)
print(arr[1, 1:2])
print("Returning index 2 from both arrays",arr[0:, 2])
print("return index 2 to 5 from both the rows", arr[0:2,2:5])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print("datatype is  " ,arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

try : 
  arr = np.array(['a', '2', '3'], dtype='i') #will raise value error 
except Exception as e:
  print(e)

ne_aar = arr4.astype('f') # to change datatype of array
print(ne_aar)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)


