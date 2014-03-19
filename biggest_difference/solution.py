def biggest_difference(arr):
    difference = arr[0] - arr[1]
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i] - arr[j] < difference:
                difference = arr[i] - arr[j]
            if arr[j] - arr[i] < difference:
                difference = arr[j] - arr[i]
    return difference