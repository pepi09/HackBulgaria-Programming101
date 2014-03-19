def prepare_meal(number):
    string = ""
    if number % 3 == 0:
        num = number
        n = 0
        while num % 3 == 0:
            num = num // 3
            n+=1
        string += "spam"
        n-=1
        while n > 0:
            string += " spam"
            n-=1
    if number % 5 == 0:
        if len(string) == 0:
            string += "eggs"
        else:
            string += " and eggs"
    return string