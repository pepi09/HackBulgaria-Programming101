def sum_of_min_and_max(arr):
    min = arr[0]
    max = arr[0]
    for i in range(0,len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return min + max