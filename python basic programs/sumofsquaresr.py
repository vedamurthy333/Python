def sum(n):
    if n<=0:
        return n
    else:
       
        
       return n*n+sum(n-1)
        

n=int(input("Enter the value of n:"))
print("Sum of n natural numbers are",sum(n)) 