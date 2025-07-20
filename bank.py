def deposit(Accounts, amt, ch):
    Accounts[ch] += amt
    print(f"₹{amt} deposited successfully.")
def withdraw(Accounts, amt, ch):
    if Accounts[ch] >= amt:
        Accounts[ch] -= amt
        print(f"₹{amt} withdrawn successfully.")
    else:
        print("Insufficient balance.")
def transfer(Accounts, amt, from_acc):
    to_acc = int(input("Enter the account number to transfer to: "))
    if to_acc not in Accounts:
        print("Target account does not exist.")
        return
    if Accounts[from_acc] >= amt:
        Accounts[from_acc] -= amt
        Accounts[to_acc] += amt
        print(f"₹{amt} transferred successfully to Account {to_acc}.")
    else:
        print("Insufficient balance for transfer.")
def menu(Accounts, ch):
    while True:
        print(f"\nWelcome Account {ch}")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. TRANSFER")
        print("5. LOGOUT")
        d = int(input("Enter your choice: "))
        if d == 1:
            print("Balance is ₹", Accounts[ch])
        elif d == 2:
            amt = int(input("Enter the amount to deposit: ₹"))
            deposit(Accounts, amt, ch)
        elif d == 3:
            amt = int(input("Enter the amount to withdraw: ₹"))
            withdraw(Accounts, amt, ch)
        elif d == 4:
            amt = int(input("Enter the amount to transfer: ₹"))
            transfer(Accounts, amt, ch)
        elif d == 5:
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")

Accounts = {101: 1000, 102: 2000, 103: 3000}
while True:
    print("------BANK MANAGEMENT SYSTEM------")
    ch = int(input("Enter Account Number (0 to exit): "))
    if ch == 0:
        print("Exiting the system.")
        break
    elif ch in Accounts:
        menu(Accounts, ch)
    else:
        print("Invalid Account number.")