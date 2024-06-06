print(0)
print(1)
count = 2

def fibo(prev0,prev1):
    global count
    if(count<=19):
        new_num = prev0+prev1
        print(new_num)
        prev0 = prev1
        prev1 = new_num
        count+=1
        fibo(prev0,prev1)
    else:
        return
    
fibo(0,1)   
