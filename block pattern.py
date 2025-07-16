b=int(input("Enter no of blocks:"))
l=int(input("Enter no of lines:"))
s=int(input("Enter no of starts:"))
sum=0
print("--------------")
for i in range(b):
  print(f"------BLOCK{i+1}----")
  count=0
  for j in range(l-i):
    for k in range(s):
      print("*",end=" ")
      count=count+1
    print()
  print(count)
  sum+=count
print(f"Total:{sum}")