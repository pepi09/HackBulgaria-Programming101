def is_an_bn(word):
    if word == "":
        return True
    n = 0
    i = 0 
    while word[i] == 'a' :
        n += 1
        i += 1
    if n == len(word)/2:
        return True
    else:
        return False