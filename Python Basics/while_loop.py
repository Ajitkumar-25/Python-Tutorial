# while loop
i = int(input("Enter any number"))
while i <= 20:
    print(i)
    i = i+2

count = 5
while count > 0:
    print(count)
    count = count-1


# do while loop
i = 10
while i < 100:
    print(i)
    i = i+1
    if i == 50:
        break
    else:
        continue
