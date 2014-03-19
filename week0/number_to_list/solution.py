def number_to_list(n):
    arr = []
    i = 0
    while n != 0:
        arr.insert(i,n%10)
        i = i + 1
        n = n//10
    arr.reverse()
    return arr