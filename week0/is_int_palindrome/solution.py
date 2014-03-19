def is_int_palindrome(n):
    arr = []
    i = 0
    while n != 0:
        arr.insert(i,n%10)
        i = i + 1
        n = n//10
    k = len(arr) - 1
    j = 0
    arr.reverse()
    while j <= k and arr[j] == arr[k]:
        j = j+1
        k = k-1
    if j > k:
        return True
    else: 
        return False
