def get_min(arr,n):
    
    ans = arr[0]
    for i in range(1,n):
        ans = min(ans,arr[i])
    return ans
        
def get_max(arr,n):
    ans = arr[0]
    for i in range(1,n):
        ans = max(ans,arr[i])
    return ans 
        
        
arr = [2,5,7,22,5,9]      
n=len(arr)

print(get_min(arr,n))
print(get_max(arr,n))
