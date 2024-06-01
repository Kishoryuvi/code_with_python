def count_occurrences(arr,n,x):
    ans = 0
    for i in range(1,n-1):
        if(arr[i]==x):
            ans +=1
            
    return ans
    
arr = [1,2,2,2,2,5,5,6]  
n = len(arr)
x=2

print(count_occurrences(arr,n,x))
