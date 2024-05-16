def print_reverse_table(n):
    multiplier = 10
    while(multiplier>0):
       print(n*multiplier, end=" ")
       multiplier -=1
       
print("enter the number")
n = int(input())
print_reverse_table(n)  
