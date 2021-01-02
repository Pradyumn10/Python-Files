"""
#1.Calculator
sum = int(input("Enter First Number:"))
c=input("Enter operation:")
def a(c):
    if c=="+":
        z = int(input("Enter Next Number:"))
        global sum
        sum=sum + z
        print(sum)
        c=input("Enter next operation or enter exit:")
        a(c)
    elif c=="*":
         z = int(input("Enter Next Number:"))
         sum=sum * z
         print(sum)
         c=input("Enter next operation or enter exit:")
         a(c)
    elif c=="/":
        z = int(input("Enter Next Number:"))
        sum=sum / z
        print(sum)
        c=input("Enter next operation or enter exit:")
        a(c)
    elif c=="-":
        z = int(input("Enter Next Number:"))
        sum=sum - z
        print(sum)
        c=input("Enter next operation or enter exit:")
        a(c)
    else :
        exit()         

a(c)

#2. Banking
Name=input("Enter Your Name : ")
Account_no=int(input("Enter Your Account Number : "))
balance=float(input("Enter Your Balance : "))
witha=0
depo=0
def withdrwal():
    global balance
    amount=float(input("Enter Amount : "))
    if amount<=balance:
        print("Withdrwal Sucessfull")
        balance=balance-amount
        global witha
        witha=witha+amount
        actions()
    else:
        print("Enter Value less than your balance")
        withdrwal()
def deposit():
    global balance
    amount=float(input("Enter Amount : "))
    if amount<=100000:
        print("Deposit Sucessfull")
        balance=balance+amount
        global depo
        depo=depo+amount
        actions()
    else:
        print("Enter Value less than 100000 Rs")
        deposit()
def actions():
    print("\nSelect Action : ")
    global action
    action = int(input("1.Withdrawal \n2.Deposit \n3.Get Information\n4.Exit\n"))
    if action==1:
       withdrwal()
    elif action==2:
         deposit()
    elif action==3:
         print("Name : {}".format(Name))
         print("Account Number: {}".format(Account_no))
         print("Current Balance is {}".format(balance))
         print("Total Withdrwal is {}".format(witha))
         print("Total Amount Deposited is {}".format(depo))
    elif action==4:
         print("Thank you for banking with us")                 
    else:
        print("Enter Proper value")
        actions()
actions()    


fileptr = open("file.txt","r+")
a=fileptr.read()
fileptr.write("Python is a wonderful language\n ")
print(a)
fileptr.close()
"""
import pandas as pd
a = pd.Series(Data, index = Index) 
