import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='S')
# string array
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
# int array
print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays

arr = np.array([1.1, 2.1, 3.1])
# float type by default
newarr = arr.astype('i')
# int type
print(newarr)
print(newarr.dtype)


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
