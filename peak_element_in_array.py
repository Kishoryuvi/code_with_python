def find_peak(arr,n):
    
    if(n==0):
        return 0
        
    for i in range(1,n-1):
        if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            return arr[i]
            
arr = [1,2,5,15,6,9]
n = len(arr)

print(find_peak(arr,n))
