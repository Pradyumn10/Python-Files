import random
import math
print(random.randint(0,20))
print(math.sin(90))

def dice():
    choice=int(input("roll the dice-1 \n exit-2\n"))
    if(choice==1):
        a=random.randint(1,6)
        print(a)
        dice()
    elif(choice==2):
        print("THANK YOU")
dice()
