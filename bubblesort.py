def bubble(element):
    n=len(element)
    for i in range(n):
        for j in range(n-1-i):
            if element[j]>element[j+1]:
                element[j],element[j+1]=element[j+1],element[j]
    return element            
    
element=[10,12,2,5,7,100,87]
res=bubble(element)
print(res)