# mutating tuple using converting to a list and again to a tuple
countries = ("span", "india", "japan", "russia", "germany")
l = list(countries)
l.append("china")
l.pop(3)
l[2] = 'finland'
countries = tuple(l)
print(countries)


# concatenation of two tuple
tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7, 8, 9, 10)
tup3 = tup1 + tup2
print(tup3)

# unpacking of tuple
tup = (1, 2, 3, 4, 5)
a, b, c, d, e = tup
print(a, b, c, d, e)

# unpacking of tuple using * operator
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a, b, c)
print("count of 1 is",tup.count(4))
print("index of 1 is",tup.index(4))
print("length of tuple is",len(tup))
print("max of tuple is",max(tup))
print("min of tuple is",min(tup))
print("sum of tuple is",sum(tup))
print("sorted tuple is",sorted(tup))

# tuple comprehension
tup = (1, 2, 3, 4, 5)
tup1 = tuple(i for i in tup if i % 2 == 0)
print(tup1)

# tuple comprehension using map
tup = (1, 2, 3, 4, 5)
tup1 = tuple(map(lambda x: x * 2, tup))
print(tup1)

# tuple comprehension using map and filter
tup = (1, 2, 3, 4, 5)
tup1 = tuple(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, tup)))
print(tup1)






