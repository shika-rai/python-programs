a="aaabbcccccaa"
c=1
res=""
for i in range(len(a)):
    if(i+1<len(a) and (a[i]==a[i+1])):
        c=c+1
    else:
        res=res+a[i]
        res=res+str(c)
        c=1
print(res)