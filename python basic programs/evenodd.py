

def oddeven(a):

    for i in a:
        if i % 2==0:
           even.append(i)
           print(i,"is even number")
        else:
           odd.append(i)
           print(i,"is odd number")

    print("even numbers are:",even)
    print("odd numbers are:",odd)
    

n=int(input("Enter the value of n:"))
a=[]
even=[]
odd=[]
while n > 0:
    value=int(input("Enter the value:"))
    a.append(value)
    n=n-1
print("Inputed values are:", a) 
oddeven(a)  

    

