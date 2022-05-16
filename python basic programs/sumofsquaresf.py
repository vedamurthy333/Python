def sum(n):
    if n<=0:
        return n
    else:
        return (n*(n+1)*(2*n+1))/6

n=float(input("Enter the value of n:"))
print("sum of squares of natural numbers are:",(sum(n)))            