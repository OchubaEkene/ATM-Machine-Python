balance = 10000
print("""
Welcome to ATM Machine

Choose Transaction

1)BALANCE
2)WITHDRAW
3)DEPOSIT
4)EXIT

""")
option = int(input("Enter Transaction: "))

if(option == 1):
    print("Your balance is: ", balance)
elif(option==2):
    withdraw = float(input("Enter amount to withdraw: "))
    if(balance > withdraw):
        total = balance - withdraw
        print("Success!")
        print("your new balance is :",total)
    else:
        print(Insufficient Balance")
elif(option==3):
    deposit = float(input("Enter amount to deposit: "))
    totalbalance = balance + deposit
    print("Success!")
    print("total balnace now is: ", totalbalance)
elif(option==4):
    exit()
else:
    print("No selected transaction")
