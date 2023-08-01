a = "ha rry 123 @@@@@"
print(len(a))
print(a.lower())
print(a.upper())
print(a.rstrip("@"))
print(a.replace("@", "$"))
print(a.split(" "))

heading = "this is a heading and needs to be capitalize"
print(heading.capitalize())
print(heading.title())


print(a.count("@"))
print(a.find("@"))
print(a.find("r"))
print(a.find("r", 4, 6))
print(a.endswith("@"))
print(a.index("rr"))

str1="abcd1234"
str2="abcd"
str3="123"
print(str1.isalnum())
print(str2.isalpha())
print(str3.isdigit())
print(str2.islower())

