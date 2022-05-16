def area(b,h):
    area=0.5*b*h
    return area

def perimeter (i,b,h):
    perimeter=l+b+h
    return perimeter

l=int(input("Enter the value of length:"))
b=int(input("Enter the value of breadth:"))
h=int(input("Enter the value of height:"))
print("Area of triangle is:",area(b,h))
print("Perimeter of triangle is:",perimeter(l,b,h))        