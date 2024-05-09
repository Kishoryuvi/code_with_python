def print_even(n):
    for i in range(1,n+1):
        if(i%2==0):
            print(i)
            
print("Enter the number")
n=int(input())
print_even(n)
