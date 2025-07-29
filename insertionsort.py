def insertion(element):
    n=len(element)
    for i in range(1,n):
        key=element[i]
        j=i-1
        while j>=0 and element[j]>key:
            element[j+1]=element[j]
            j-=1
        element[j+1]=key
    return element


element=[10,12,2,5,7,100,87]
res=insertion(element)
print(res)