s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))

#intersection
print(s1.intersection(s2))

#difference
print(s1.difference(s2))

#symmetric difference
print(s1.symmetric_difference(s2))

#subset
s3={1,2,3,4,5}
s4={1,2,3}
print(s4.issubset(s3))

#superset
print(s3.issuperset(s4))

#disjoint
print(s1.isdisjoint(s2))

#frozen set
s5=frozenset([1,2,3,4,5])
print(s5)

# add method
s1.add(6)
print(s1)

#remove method
s1.remove(6)
print(s1)

#discard method
s1.discard(5)
print(s1)

#pop method
s1.pop()
print(s1)

#clear method
s1.clear()
