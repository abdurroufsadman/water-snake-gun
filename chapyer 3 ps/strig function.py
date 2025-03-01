name ="harry"
print(len(name))
print(name.endswith("rray")) # it will return false as the string does not end with "rray"  
print(name.startswith("har")) # it will return true as the string starts with "har"
print(name.capitalize())# it will capitalize the first letter of the string
print(name.upper())# it will capitalize the whole string
print(name.lower())# it will make the whole string lower case
print(name.title())# it will capitalize the first letter of each word in the string
print(name.strip())  # Output: harry # it will remove the white spaces from the start and end of the string
print(name.lstrip())  # Output: harry # it will remove the white spaces from the start of the string
print(name.replace("r", "z"))  # Output:  hazzy # it will replace the first argument with the second argument 
print(name.find("a"))  # Output: 1 # it will return the index of the first occurence of the argument
print(name.split("r"))  # Output: ['ha', '', 'y'] # it will split the string at the argument and return a list
