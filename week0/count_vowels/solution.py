def count_vowels(str): 
    string = str.lower()
    counter = 0
    for k in range(0,len(string)):
        if string[k] == 'e'or string[k] == 'y' or  string[k] == 'u' or string[k] == 'i' or  string[k] == 'o' or string[k] == 'a': 
            counter = counter + 1 
    return counter