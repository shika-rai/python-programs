a=int(input("Enter number:"))
tot=0
while(a>0):
    tot=tot+a%10
    a=a//10
print("the sum of digit is",tot)    