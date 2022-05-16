
def sum(n):
     if n<0:
         return n
     else:

         return n + sum(n-1)
     

n=int(input("Enter the value of n:"))
if n < 0:
    print("Enter positive number!!!")
else:    
    a=sum(n)
    print(a)