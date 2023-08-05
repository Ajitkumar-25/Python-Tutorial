def binary_search(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=int(input("Enter Integer to be saerched: "))
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")



# default arguments
def sum(a=1,b=6):
    print("sum is: ",a+b)
sum(10,20)

# keyword arguments
def sum(a,b):
    print("sum is: ",a+b)
sum(b=10,a=20)

# variable length arguments
def sum(*a):
    print(type(a))
    s=0
    for i in a:
        s=s+i
    print("sum is: ",s)
sum(10,20,30,40,50)

# keyword variable length arguments
def person(name,**data):
    print(name)
    print(data)
    print(type(data))
person('navin',age=28,city='mumbai',mob=1234567890)

# lambda function
f=lambda a,b:a+b
result=f(10,20)
print(result)

