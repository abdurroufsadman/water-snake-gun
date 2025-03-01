import math

n = int(input("Enter a number: "))

if n < 2:  # Numbers less than 2 are not prime
    print("Number is not prime")
else:
    for i in range(2, int(math.sqrt(n)) + 1):  # Check up to sqrt(n)
        if n % i == 0:
            print("Number is not prime")
            break
    else:  # Executes only if the loop completes without finding a divisor
        print("Number is prime")
