def si(p,t,r):
    rate=r/100
    simpleinterest=(p*t*rate)/100
    return simpleinterest

p=float(input("Enter the value of principle:"))
t=float(input("Enter the value of time:"))
r=float(input("Enter the value of rate:"))
print("si is",si(p,t,r))    