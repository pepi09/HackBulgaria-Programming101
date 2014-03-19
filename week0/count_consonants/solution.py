def count_consonants(str):
    string = str.lower()
    counter = 0
    for k in range(0,len(string)):
        if string[k] != 'e' and string[k] != 'y' and  string[k] != 'u' and string[k] != 'i' and string[k] != 'o' and string[k] != 'a': 
            counter = counter + 1 
    return counter