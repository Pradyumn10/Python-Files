#functions
import math

x= math.tan(90)
print(x)
print("Functions")
def sayhello():
    print("Hello! Welcome to PYTHON IDLE")

sayhello()

def add(a,b):
    c=a+b
    print(c)
add(7,10)

def multiply(a,b,c=10):
    d=a*b*c
    print(d)

print("Arguments")
multiply(5,4,3)

print("Required Argument")
multiply(5,4)


print("Keyword Argument")
multiply(a=15,b=4,c=3)

print("Default Argument")
multiply(7,8)

def python(a):
    print(a)
    
print("Variable-length Argument")
q=(7,8,4)
python(q)

#Variables
print("Variables")
x=5
def loc():
    x=7
    print(x)
    def non():
        x=8
        print(x)
    non()
print(x)
loc()
def loc1():
    print("Global")
    global x
    x=7
    print(x)
    def non():
        print("Non-local")
        nonlocal x
        x=8
        print(x)

loc1()