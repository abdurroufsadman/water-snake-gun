
def f_to_c(f):
    return 5*(f-32/9)
f=float(input("Enter the temperature in fahrenheit: "))
# print(f"The temperature in celsius is {f_to_c(f)}"))
# print(f_to_c(32))
# print(f"{f_to_c(f):.2f}\u00B0C") . it will put the degree symbol

# print(f"{f_to_c(f)} °C") . it will also put the degree symbol
c=f_to_c(f) # c have to be defined before using it in the print statement
print(f"{round(c,2)} °C")
print("thank you")   


# here each print line can be used to print the output. The last print statement is used to print the output. The other print statements are used to check the output.
# The output is as follows: