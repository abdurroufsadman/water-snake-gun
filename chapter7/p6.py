#for loop
n=int(input("Enter a number : "))

product=1
for i in range(1,n+1):
    product=product*i
    

print (f"the factorial of {n} is {product}")

#whie  loop
n = int(input("Enter a number: "))

product = 1
i = 1

while i <= n:
    product *= i
    i += 1

print(f"The factorial of {n} is {product}")
