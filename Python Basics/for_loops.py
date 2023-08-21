for i in range(0, 10):
    if (i % 2 == 0):
        print(i)
    else:
        print("something wrong")

print('\n')


str = "ajitkumar"
for i in str:
    print(i)


friends = ["himashu", "kamal", "ashutosh", "monic"]

for friend_name in friends:
    print('Hello', friend_name, 'welcome to my website.')
    for i in friend_name:
     print(i)

detail={"name":"Himanshu","age":21,"batch":"B11"}
for key,value in detail.items():
    print("{} is {}".format(key, value))



