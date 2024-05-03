def print_reverse(n):
    
    reverse = 0
    while(n>0):
        temp = n%10
        reverse = reverse*10 + temp
        n = n//10
    return(reverse)
    
print("Enter the number: ")   
n = int(input())
print(print_reverse(n))
