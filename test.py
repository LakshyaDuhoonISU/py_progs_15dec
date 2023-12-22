import bank
b=bank.ATM()
while True:
    a=int(input("Press 1 to deposit\nPress 2 to withdraw\nPress 3 to check balance\nPress 4 to Exit\n"))
    if a==1:
        b.deposit()
    elif a==2:
        b.withdraw()
    elif a==3:
        b.check()
    elif a==4:
        print("Thank You")
        break
    else:
        print("Invalid choice\n")
