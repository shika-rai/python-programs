a=int(input("Enter a num1:"))
b=int(input("Enter a num2 :"))
if(a>b):
  big=a
else:
  big=b
step=big
while(True):
  if(big%a==0 and big%b==0):
    print("The lcm is: ", big)
    break
  else:
    big=big+step