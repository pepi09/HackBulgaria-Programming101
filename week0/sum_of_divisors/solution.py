def sum_of_divisors(n):
    if n < 0:
        n = abs(n)
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum = sum + i
    return sum