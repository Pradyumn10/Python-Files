def p1(n): 
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(" * ",end="") 
        print("\r") 
def p2(n):  
    k = 2*n - 2 
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 2
        for j in range(0, i+1): 
            print("* ", end="") 
        print("\r") 

def p3(n):  
    k = n - 1 
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 1
        for j in range(0, i+1): 
            print("* ", end="") 
        print("\r") 
