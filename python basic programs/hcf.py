def hcf(a,b):
    if a > b:
        small= b
    else:
        small= a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            hcf=i
          
    return hcf

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("hcf of",a,"and",b,"is",hcf(a,b))    
