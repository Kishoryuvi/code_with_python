def factorial(n):
    
    factorial=1
    
    if(n<1):
        print("not valid")
    elif(n==0):
        print("factorial is 0")
        
    else:
        for i in range(1,n+1):
            factorial = factorial*i
        return factorial
        
print(factorial(5))        
            
