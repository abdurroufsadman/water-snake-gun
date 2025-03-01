def pattern(n):
    if (n==0):
        return  # when the base case is reached, the recursion will stop

    print("*"*n)
    pattern(n-1)

pattern(5) # this is also recursion