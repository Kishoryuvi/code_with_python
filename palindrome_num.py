def palindrome_num(n):
    
    temp = n
    rev = 0
    
    while(temp>0):
        a = temp%10
        rev = rev*10+a
        temp = temp//10
        
    if(rev == n):
        print("palindrome number")
    else:
        print("not a palindrome number")
        
print(palindrome_num(12321))     
