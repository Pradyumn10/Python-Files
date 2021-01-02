a={}
b=[]
def Issue():
    global b
    ba=input("Enter date in DD-MM-YY format ")
    b=[s_id,b_id,ba]
    global a
    a={s_id:ba}
    print("Issue Successful",a)
    Library()

def Reutrn():
    ab=int(input("Enter book id"))
    global b
    if b_id==ab:
        return_date=input("Enter Return date in DD-MM-YY format")
        b.remove(b_id)
        global a
        a={s_id:b}
        print("Return Successful")
    else:
        print("No book")
    Library()

def Library():
    print("1.Issue Book \n 2.Return Book \n 3.Details \n 4.Exit")
    inp=int(input("Enter your choice "))
    if inp==1:
        Issue()
    elif inp==2:
        Reutrn()
    elif inp==3:
        print(b)
    elif inp==4:
        print("Thank you!!")
    else:
        print("Enter proper choice")
        Library()

name=input("Enter Name ")
s_id=int(input("Enter your Student ID "))
b_id=int(input("Enter the Book ID "))
Library()
