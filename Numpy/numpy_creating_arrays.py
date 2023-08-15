import numpy as np

# numpy version
# print(np.__version__)


# Create a 0-D array with value 42
arr2 = np.array(42)

print(arr2)

# Create a 1-D array containing the values 1,2,3,4,5:
arr3 = np.array([1, 2, 3, 4, 5])
print(arr3)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr5)

# Check how many dimensions the arrays have:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Higher Dimensional Arrays
# An array can have any number of dimensions.

arrr = np.array([1, 2, 3, 4], ndmin=5)

print(arrr)
print('number of dimensions :', arrr.ndim)
