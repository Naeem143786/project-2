balance = 5000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")