d={} #empty dictionary
marks ={
    "Harry":100,
    "Shubham":56,
    "Rohan":23,
    "list1":[1,2,3,4,5]
}

print(marks,type(marks))#<class 'dict'> dictionary is a key value pair. prints everything in the dictionary
print(marks["Harry"])#print the value of the key
print(marks["Shubham"])
#properties of dictionary
#1. dictionary is mutable  
#2. dictionary is unordered
#3. dictionary is indexed
#4. cannot contain duplicate keys
#5. can contain duplicate values
#6. can contain any data type
print(len(marks))#prints the length of the dictionary