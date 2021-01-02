#table using lambda function
print("Table using lambda function")
x=(1,2,3,4,5,6,7,8,9,10)
a=int(input("Enter number=> "))
b=tuple(map(lambda x: x*a,x))
print(b)

#* method
x2={1:"Fortnite",2:"is",3:"great"}
print(*x2)
print("\n")
#decorator
print("Decorator")
def hello_decorator(func):
    def inner1():
        print("this is before execution")

        func()

        print("this is after execution ")
    return inner1
@hello_decorator
def function_to_be_used():
    print("this is inside func")

#function_to_be_used=hello_decorator(function_to_be_used)
function_to_be_used()

#list(filter(lambda x:(x%3 == 0),List))