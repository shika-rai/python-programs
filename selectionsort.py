def selection(element):
    n=len(element)
    for i in range(n):
        min=element[i]
        for j in range(i+1,n):
            if element[j]<min:
                
             min,element[j]=element[j],min
        element[i]=min     
    return element            




element=[10,12,2,5,7,100,87]
res=selection(element)
print(res)