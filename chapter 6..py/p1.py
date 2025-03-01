a1= int(input("Enter number 1:"))# why int? input function's output is string . that's why use int to typecast
a2= int(input("Enter number 1:"))
a3= int(input("Enter number 1:"))
a4= int(input("Enter number 1:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:",a1)
elif(a2>a3 and a2>a1 and a2>a4):
    print("Greatest number is a2:",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is:",a3)
else:
    print("Greatest number is:",a4)
