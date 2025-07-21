import random
name1 = input("Enter player 1: ")
name2 = input("Enter player 2: ")

print("Computer has fixed 5 numbers in the range 1 to 10.")
print("You have to guess them... Ready!")
nums = []
while len(nums) != 5:
    d = random.randint(1, 10)
    if d not in nums:
        nums.append(d)

print("--------------")
s1 = 0
s2 = 0
player1 = []
player2 = []
for i in range(3):
    print("---- ROUND {} ----".format(i + 1))
    print("Dear {}, guess your choice:".format(name1))
    ch = int(input())
    while ch in player1 or ch in player2:
        ch = int(input("It is already taken, choose another: "))
    player1.append(ch)
    if ch in nums:
        print("--->> CORRECT!")
        s1 += 1
    else:
        print("----->> WRONG")
    print("Dear {}, guess your choice:".format(name2))
    ch = int(input())
    while ch in player1 or ch in player2:
        ch = int(input("It is already taken, choose another: "))
    player2.append(ch)
    if ch in nums:
        print("--->> CORRECT!")
        s2 += 1
    else:
        print("----->> WRONG")

    print("------------")
    print("Round Summary:")
    print("{}'s guesses so far: {} | Score: {}".format(name1, player1, s1))
    print("{}'s guesses so far: {} | Score: {}".format(name2, player2, s2))
    print("------------")

print("===== FINAL RESULT =====")
print("Computer's numbers were:", nums)
print("{}'s final score: {}".format(name1, s1))
print("{}'s final score: {}".format(name2, s2))

if s1 > s2:
    print(" {} wins!".format(name1))
elif s2 > s1:
    print(" {} wins!".format(name2))
else:
    print("It's a TIE!")
