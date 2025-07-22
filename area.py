def cir():
    r=int(input("Enter the radius:"))
    res=3.14*r*r
    print("Area of circle=",res)
def sq(s):
    print("Area of square=",s*s)
    
def tri():
    l=int(input("Enter the length:"))
    h=int(input("Enter the height:"))
    return (1/2)*l*h

def rec(l,b):
    return (l*b)

print("1.CIRCLE")
print("2.SQUARE")
print("3.TRIANGLE")
print("4.RECTANGLE")
print("0:Exit")
ch=1
while(ch>0):
    print("Enter your choice:")
    ch=int(input())
    match ch:
        case 1:
            cir()
        case 2:
            a=int(input("Enter the side:"))
            sq(a)
        case 3:
            res=tri()
            print("Area of triangle=:",res) 
        case 4:
            l=int(input("Enter the length:"))
            h=int(input("Enter the height:"))
            res=rec(l,h)
            print("Area of rectangle=",res)
        case 0:
            exit()
        case _:
            print("Invalid")