def contains_digit(number, digit):
    while number != 0:
        if number % 10 == digit:
            return True
        number = number // 10
    return False

def contains_digits(number, digits):
    flag = True
    i = 0
    while i < len(digits) and flag == True:
        if not contains_digit(number,digits[i]):
            flag = False
        i = i + 1
    if flag == True:
        return True
    else:
        return False