'''n=int(input("Enter a number"))
k=2*n-2

for i in range (0,n):

    #printing spaces
    for j in range(0,k):
        print(end=' ')
    k=k-1

    for j in range(0,i+1):
        print("*",end='')
    
    print("")'''
def triangle(n): 
      
    
    k = 2*n-2
  
     
    for i in range(0, n): 
      
        
         
        for j in range(0, k): 
            print(end=" ") 
      
        
        k = k - 1
      
         
        for j in range(0, i+1): 
          
            print("* ", end="") 
      
         
        print("\r") 
  

n = 5
triangle(n)
    
