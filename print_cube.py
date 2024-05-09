def print_cube(n):
    i=1
    while(i<n+1):
        if(i*i*i < n+1):
            print(i*i*i)
            i+=1
        
print("Enter the number:")
n=int(input())
print_cube(125)        
        
