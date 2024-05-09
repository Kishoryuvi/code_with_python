def print_cube_series(n):
    for i in range(1,10000000):
        if(i*i*i < n+1):
            print(i*i*i)
            
print("Enter the number:")
n = int(input())
print_cube_series(n)
        
