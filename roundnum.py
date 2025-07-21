n = int(input("Enter any number"))
l = []
while(n not in l):
    l.append(n)
    n = sum([(int(i)*int(i)) for i in str(n)])
if n == 1:
    print("It is a round number")
else:
    print("Not a round number")