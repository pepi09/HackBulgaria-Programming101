def sevens_in_a_row(arr, n):     
    count = 0     
    for i in range(0,len(arr)):
        if arr[i] == 7:             
            k = i             
            while k < len(arr) and arr[k] == 7:                 
                count = count + 1                
                k = k + 1         
        if count == n:             
            return True         
        else:             
            count = 0
    return False
