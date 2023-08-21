a = {
    "name": "Rajesh",
    "age": 25,
}
print(a["name"])

b = {
    1: "4",
    2: "5",
    3: "6"
}
print(b[1])
print(b.get(1))


data = {'name': 'ajit',
        'age': 25,
        'address': 'pune',
        'phone': 1234567890}

print(data.keys())

for key in data.keys():
    print(key, ":", data[key])

print(data.items())   

for key, value in data.items():
    print(key, ":", value)
