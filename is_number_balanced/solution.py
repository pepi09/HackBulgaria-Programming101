def is_number_balanced(n):
    arr = []
    i = 0
    while n != 0:
        arr.insert(i,n%10)
        i = i + 1
        n = n//10
    k = len(arr)-1
    j = 0
    arr.reverse()
    sum_back = 0
    sum_front = 0
    while j < k:
        sum_front = sum_front + arr[j]
        sum_back = sum_back + arr[k]
        j = j + 1
        k = k - 1
    if sum_front == sum_back:
        return True
    else:
        return False