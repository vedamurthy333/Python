def sum(n):
    if n<=0:
        return n
    else:
        sum=0
        for i in range(1,n+1):
            sum=sum+(i*i)
        return sum

n=int(input("Enter the value of n:"))
print("Sum of n natural numbers are",sum(n))              