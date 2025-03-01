a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
#function definition
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c
print(greatest(a,b,c))# function call
print("thank you ")