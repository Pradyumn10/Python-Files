print("WELCOME TO THE CALCULATOR")


#x=int(input("Enter first number"))
x=0
choice='yes'
total=0

while choice=='yes':
    x=total
    if x==0:
        x=int(input("Enter first number"))  

    c=input("Enter the operator")
    y=int(input("Enter second number"))
    
    def opcheck(i,j,k):
        if c=='+':
            total=x+y
            print("Sum = ",total)
            
        elif c=='-':
            total=x-y
            print("Difference",total)
            
        elif c=='*':
            total=x*y
            print("Product = ",total)
            
        elif c=='/':
            total=x/y
            print("Quotient = ",total)
        
        elif c=='%':
            total=x%y
            print("Remainder = ",total)
            
        else:
             print("Wrong operator")
    
    opcheck(x,y,c)
    x=total
    choice=input("enter yes to do more operations")
    
    
    
    
