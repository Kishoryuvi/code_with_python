def print_digit(n):
    
    while(n>0):
        temp = n%10
        n = n//10
        print(temp)
        
print("Enter the number: ") 
n = int(input())
print_digit(n)
