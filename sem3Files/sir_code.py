n=int(input("Enter number"))

for i in range (0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("#",end=" ")
    print("")
for i in range (0,n-i):
    for j in range(0,(n-i)-i-1):
        print(end=" ")
    for j in range(0,n+1):
        print("#",end=" ")
    print("")
