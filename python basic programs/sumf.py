def sum(n):
    if n < 0:
        return n
    else:
      return (n*(n+1))/2


n=int(input("Enter the n value:"))
if n < 0:
    print("enter the positive number!!")
else:
    print(sum(n))           
            