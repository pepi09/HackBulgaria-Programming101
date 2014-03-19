def unique_words_count(arr):
    words = []
    for i in range(0,len(arr)):
        if not arr[i] in words:
            words.append(arr[i])
    return len(words)
