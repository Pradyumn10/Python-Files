"""#loops
      #for loop
i=0
print("\n For loop \n")
for i in ("Hello"):
    print(i)

       #while loop

print("\n While loop \n")
c=6
j=0
while j<11:
    d=j*c
    print("{} * {} = {}".format(c,j,d))
    j+=1

#list

print("\n List \n")    
thislist = ["BMW","AUDI","FERRARI"]

print(thislist[1])
    
#Tuples

print("\n Tuples \n")
thistuple = ("BMW","AUDI","FERRARI")
print(thistuple)

#Set

print("\n Set \n")
thisset = {"BMW","AUDI","FERRARI"}
secondset={"Cars"}
thisset.add("Rolls Royce")#single elements
thisset.update("Lambo","VW")#multiple elements
print(thisset|secondset)#union
print(thisset.union(secondset))#union
print(thisset-secondset)
print(thisset)

#dict

print("\n Dictionary \n")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i is thisdict.values():
    print(i)

#conditional statements

      #If-else
print(" \n If - else statement \n")
a,b=5,10
if a>b :
    print("a is greater than b")
else:
    print("b is greater than a")
     
        #elif
print(" \n elif statement \n")
a,b=5,5
if a>b :
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

#String Functions
    
    print("\n String Functions \n")

a = "Python, is an awesome language"
y ="         cat"
print(a.islower())
print(y.strip())
print(a.replace("a","C"))
    print(a.upper())
print(a[1:9])
print(a.split(','))
print(a.isspace())
print(a.endswith("e"))
print(a*2)
print(a.__add__(y))

print("Table using lambda function")
x=(1,2,3,4,5,6,7,8,9,10)
a=int(input("Enter number=> "))
b=tuple(map(lambda x: x*a,x))
print(b)

#** method
x2={1:"Delhi",2:"Indore",3:"Bhopal"}
print(*x2)
print("\n")
"""

#packing/unpacking
def abc(*a,**b):
    for i in b.items():
        print("Value",i)
    return a,b
print(abc(1,2,3,m=8,n=9,l=7))
