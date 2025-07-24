import random

def check(n, p, d):
    if n==7:
        p = 24
        print("yayy ladder")
    elif n==21:
        p=77
        print("yayy ladder")
    elif n==40:
        p=60
        print("yayy ladder")
    elif n==42:
        p=90
        print("yayy ladder")
    elif n==2:
        p=6
        print("oops snake")
    elif n==45:
        p = 30
        print("oops snake")
    elif n==96:
        p=64
        print("oops snake")
    else:
        p+=d
    return p




p1 = 0
p2 = 0
while(True):
    print(f"Player 1: {p1}")
    print(f"Player 2: {p2}")
    ch = int(input("Enter the player number: "))
    if ch ==1:
        a = random.randint(1, 7)
        print(f"Dice value: {a}")
        if(p1+a>100):
            continue
        if(p1+a==100):
            print(f"Winner is player 1")
            exit(0)
        p1 = check(p1+a, p1, a)
        
        
        print(f"Player 1: {p1}")
        print(f"Player 2: {p2}")
        print("---------------------")
        
    elif ch==2:
        b = random.randint(1, 7)
        print(f"Dice value: {b}")
        if(p2+b>100):
            continue
        if(p2+b==100):
            print(f"Winner is player 2")
            exit(0)
        p2 = check(p2+b, p2, b)
        
        
        
        print(f"Player 1: {p1}")
        print(f"Player 2: {p2}")
        print("---------------------")
    elif ch==0:
        print("Exiting")
    else:
        print("Invalid")


