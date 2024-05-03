def armstrong_num(n):
    temp = n
    sum = 0
    
    while(temp>0):
        a = temp%10
        sum += a**3
        temp = temp//10
        
    if(sum == n):
        return True
    else:
        return False
    
print("Enter the number")
n = int(input())
print(armstrong_num(n))
