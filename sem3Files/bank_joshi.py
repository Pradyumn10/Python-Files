a=0
b=0
def withdrawl():
    global balance
    amount=float(input("Enter Amount : "))
    if amount<=balance:
        print("Withdrwal Sucessfull")
        balance=balance-amount
        print(balance)
        global a
        a=a+amount
        operations()
    else:
        print("Enter proper value")
        withdrwal()
def deposit():
    global balance
    amount=float(input("Enter Amount : "))
    if amount<=10000:
        print("Deposit Sucessfull")
        balance=balance+amount
        global b
        b=b+amount
        operatons()
    else:
        print("Enter Value less than 10000 Rs")
        deposit()
def operations():
    print("\nSelect Action : ")
    global action
    action = int(input("1.Withdrawal \n2.Deposit \n3.Total Balance \n4.Exit\n"))
    if action==1:
        withdrawl()
    elif action==2:
        deposit()
    elif action==3:
        print("Name : {}".format(name))
        print("Account Number: {}".format(acc_no))
        print("Current Balance is {}".format(balance))
        print("Total Withdrwal is {}".format(a))
        print("Total Amount Deposited is {}".format(b))
    elif action==4:
        print("Thank you for banking with us")                 
    else:
        print("Enter Proper value")
        operations()

print("Welcome to Highway Bank")
name=input("Enter Your Name : ")
acc_no=int(input("Enter Your Account Number : "))
balance=float(input("Enter Your Balance : "))
if (balance>=20000):
    balance=float(input("Renter balance"))
    operations()
else:
    operations() 
