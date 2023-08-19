import numpy as np

arr=np.array([1,3,4,5,6,7,8])
print(arr[0])

print(arr[1]+arr[2])

print(arr[1]+arr[2]+arr[3])

print("\n")
# Access 2-D Arrays

arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row: ', arr2[0, 1])

# Access 3-D Array


arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3[0, 1, 2])

# negative indexing

arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr4[1, -1])