def factorial(n):
    if n <= 0:
        return 1
    else:
        fact=1
        while n>0:
            fact=fact*n
            n=n-1
        return fact
n=int(input("Enter the value of n:"))
print("factorial of",n,"is",factorial(n))                    