c = int(input("ENTER YOU AGE: "))
print('your age is ', c)

# conditional operator == != >= <=

print(c == 18)
print(c != 18)
print(c > 18)
print(c < 18)

# if else

if c < 18:
    print('you are not eligible to vote')
else:
    print('you are eligible to vote')


# elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# and
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


# or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


# nested if

x = 41
# temperature in Celsius
if x > 30:
    print("It's very hot today.")
    if x > 40:
        print("And the humidity is very high.")
else:
    print("It's not so hot today.")
