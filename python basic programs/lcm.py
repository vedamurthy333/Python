def lcm(a,b):
    if a > b:
        greater=a
    else:
        greater=b
    while(1):
       if greater % a==0 and greater % b==0:
           lcm=greater
           break
       greater+=1 
    return lcm            


a=int(input("Enter a number:"))
b=int(input("Enter the another number:"))
print("lcm of",a,"and",b,"is",lcm(a,b))
