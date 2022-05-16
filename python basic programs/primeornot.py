def prime(a):
    for p in a:

        count=0
        for j in range(1,p+1):
            if p % j==0:
                count=count+1

        if count==2:
            print(p,"is prime number")
        else:
            print(p,"is not a prime number") 

n=int(input("Enter the value of n:"))
a=[]
while n > 0:
    b=int(input("Enter the number:"))
    a.append(b)
    n=n-1
print("inserted values are:",a)    
prime(a)                   