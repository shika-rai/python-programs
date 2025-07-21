def prime_factors(n):
    for i in range(2,n+1):
        if n%i==0:
            print(i,end=" ")
            prime_factors(n//i)
            break
n=int(input("Enter any number:"))
prime_factors(n)


def prime_factors(n):
    if n==1:
        return
    i=2
    while(n%i!=0):
        i=i+1
    print(i,end=" ")
    prime_factors(n//i) 
n=int(input("Enter any number:"))
prime_factors(n)       
