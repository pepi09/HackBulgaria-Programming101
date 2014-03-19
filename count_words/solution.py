def count_words(arr):
    words = {}
    for i in range(0,len(arr)):
        if not arr[i] in words.keys():
            words[arr[i]] = occurrences(arr,arr[i])
    return words

def occurrences(arr,elem):
    count = 0
    for i in range(0,len(arr)):
        if arr[i] == elem:
            count+=1
    return count