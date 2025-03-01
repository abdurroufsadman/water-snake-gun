s={1,5,32,5,5,"Harry"}
print(s,type(s))#<class 'set'> set is a collection of non duplicate values. it is unordered and unindexed
s.add(6)#adds an element to the set
print(s,type(s))
#properties of sets
#1. set is mutable
#2. set is unordered
#3. set is unindexed
#4. set cannot contain duplicate values
s.remove(5)#removes the element from the set
print(s)
print(len(s))#prints the length of the set
s.clear()#clears the set
print(s)
