def gcd(a,b):
    small=0
    if a > b:
       small=b
    else:
       small=a
    for i in range(1,small+1):
       if a % i==0 and b % i==0:
           gcd=i
    return gcd        
   
a=int(input("Enter a number:"))
b=int(input("Enter the another number:"))
print("gcd of",a,"and",b,"is",gcd(a,b))

