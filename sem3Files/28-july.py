#this is calculator
print ("Enter the numbers")
num = int(input("First number"))#first number
prin("hello")
num1 = int(input("Second number"))#second number
total = 0.01
print('''enter symbol 
         1. + for Addition
         2. - for Subtraction
         3. * for multiplication
         4. // for quotient
         5. '%' for remainder ''')

choice= input("Enter choice")
if choice=='+':
   total = num+num1
   print ("Sum =", total)
elif choice =='-':
   total = num-num1
   print ("Difference = {}".format (total))
elif choice =='*':
   total = num*num1
   print ("Product = ",total)
elif choice =='/':
   total=num/num1
   print("Quotient =",total)
elif choice =='%':
   total=num%num1
   print("Remainder=",total)
else: ("Wrong operator")

#using == and !=
if num1==num:#==
   print ("both numbers are same")
elif num != num1:#!=
   print ("both numbers are not same")
elif num>num1 :#>
   print ("First number is grater than second number")
elif num<num1 :#<
   print("Second number is grater than first number")   
else:
   print ("error")
   #**
print ("first number raised to the power of second=",num**num1)