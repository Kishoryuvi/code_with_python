def reverse_array(arr,n):
    
    start = 0
    end = n-1
    while(start<end):
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr
    
arr = [1,2,3,4,5]
n = len(arr)

print(reverse_array(arr,n))
    
