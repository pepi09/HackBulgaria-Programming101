def count_substrings(haystack, needle):
    count = 0
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            k = 0
            while  k < len(needle) and i < len(haystack) and haystack[i] == needle[k]:
                i = i+1
                k = k+1
            if k == len(needle):
                count = count + 1
            i = i - 1
        i = i + 1
    return count