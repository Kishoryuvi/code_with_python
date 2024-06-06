my_arr = [7,3,9,12,11]
n = len(my_arr)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if(my_arr[j]>my_arr[j+1]):
            my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]
            swapped = True
    if not swapped:
        break
            
            
print(my_arr)            
