print("Table using lambda function")
x=(1,2,3,4,5,6,7,8,9,10)
a=int(input("Enter number=> "))
b=tuple(map(lambda x: x*a,x))
print(b)
