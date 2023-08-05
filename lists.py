l=[3,4,5,"hello",True,7,9]
print(l)
print(type(l))
# print(l[0])

if "ello" in l:
    print("hello is present")
else:
    print("hello is not present")

if "ell" in "hello":
    print("YES")
else:
    print("NO")    

# printing elements in list 
print(l)
print(l[0:len(l)])
print(l[1:])
print(l[3:5])


# list comprehension
list =[i*i for i in range(20)]
print(list[0:len(list):3])

list =[i*i for i in range(20) if i%2==0]
print(list[0:len(list):3])