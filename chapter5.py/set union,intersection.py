s1={1,45,6}
s2={1,45,6,7,8}

print(s1.union(s2))#prints the union of the two sets
print(s1.intersection(s2))#prints the intersection of the two sets
print(s1.difference(s2))#prints the difference of the two sets
print(s1.symmetric_difference(s2))#prints the symmetric difference of the two sets
print(s1.issubset(s2))#checks if s1 is a subset of s2
print(s1.issuperset(s2))#checks if s1 is a superset of s2
print(s1.isdisjoint(s2))#checks if s1 and s2 are disjoint sets .disjoint sets appear to be different but are actually the same  
