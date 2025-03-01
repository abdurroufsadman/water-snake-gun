def remove(l,word):
    for item in l:
        l.remove(word)
        return l
l=["harry","larry","carry","marry"]
print(remove(l,"carry"))
# tho it works but it is not the correct way to do this. and it is a problematic way .for further explanation ask AI




# another way to do this is:
def remove(l, word):
    while word in l:  # Keep removing `word` until it no longer exists in the list
        l.remove(word)
    return l  # Return the modified list

l = ["harry", "larry", "carry", "marry"]
print(remove(l, "carry"))  # Output: ['harry', 'larry', 'marry']


# another way
def remove(l, word):
    n = []  # Create an empty list to store the filtered items
    for item in l:  # Iterate over each item in the input list `l`
        if item != word:  # Check if the current item is not equal to the word to be removed
            n.append(item)  # Append the item to the new list
    return n  # Return the new list

l = ["harry", "larry", "carry", "marry"]
print(remove(l, "carry"))  # Call the `remove` function and print the result