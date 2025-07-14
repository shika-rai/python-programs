a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=0
while(b!=0):
  c=a%b
  a=b
  b=c
print(a)