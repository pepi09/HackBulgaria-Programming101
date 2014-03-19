def list_to_number(digits):
    number = 0
    for i in range(0,len(digits)):
        number = number * 10 + digits[i]
    return number