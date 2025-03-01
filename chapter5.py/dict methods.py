marks ={
    "Harry":100,
    "Shubham":56,
    "Rohan":23,
    "list1":[1,2,3,4,5],
    0:"Harry"
}
print (marks.items())#prints all the items in the dictionary in tuple form
print(marks.keys())#prints all the keys in the dictionary .things that are on the left side of the colon
print(marks.values())#prints all the values in the dictionary .things that are on the right side of the colon
print(marks.update({"Harry":99}))#updates the value of the key "Harry" to 99
print(marks.update({"Renuka":100}))#adds a new key value pair to the dictionary
print(marks)
print(marks.get("Harry"))#prints the value of the key "Harry". for unavailable keys it will return none
print(marks["Harry"])#prints the value of the key "Harry". for unavailable keys it will return an error. as it shows line 14 and 15 are different tho they show the same output
print(marks.pop("Harry"))#removes the key value pair of "Harry" from the dictionary
print(marks)
print(marks.popitem())#removes the last key value pair from the dictionary
print(marks)

