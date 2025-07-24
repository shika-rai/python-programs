def cal(x,a,b):
    m=0
    while x>0:
        x=x-a
        m=m+1
        if x==0:
            return m
        x=x+b
        m=m+1
    return m
    
print(cal(30,10,5))
print(cal(25,7,4))
    