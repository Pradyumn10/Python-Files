"""#
def hello_decorator(func):
    def Inner1():
        print("Hello ,this is before the function execution")
        func()
        print("This is after function execution")
    return Inner1
@hello_decorator  #decorator
def function_to_be_used():
    print("This is inside the function")
#function_to_be_used = hello_decoder(function_to_be_used)
function_to_be_used()"""

#packing
def sum(a,b,c,d):
    print(a,b,c,d)
d=[1,2,3,4]
sum(*d)
