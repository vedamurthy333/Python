def max(a,b,c):
    if a > b:
        if a > c:
            print(a,"is greater")
        else:
            print(c,"is greater")
    else:
        if b > c:
            print(b,"is greater")
        else:
            print(c,"is greater")  



a=int(input("Enter a first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
max(a,b,c)
  