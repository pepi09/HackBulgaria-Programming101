def sum_of_digits(n):
    if n < 0:
        n = abs(n)
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_of_digits(n//10)
        