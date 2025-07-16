s=input("Enter password:")
dg=0
up=0
lw=0
sl=0
if(len(s)>7):
  for i in s:
    if(i.isupper()):
      up=up+1
    elif(i.islower()):
      lw=lw+1
    elif(i.isdigit()):
      dg=dg+1
    else:
      sl=sl+1
  if(up>0 and lw>0 and dg>0 and sl>0):
    print("good password")
  else:
    print("bad password")
else:
  print("bad password due to less character")
