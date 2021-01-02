#generator

'''def infinte_seq():
    num=0
    while True:
        yield num
        print(num)
        num+=1
print(infinte_seq())
'''
num=0       
gen=(num**2 for num in range(5))
'''
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
for value in simpleGeneratorFun():  
    print(value) 
'''
