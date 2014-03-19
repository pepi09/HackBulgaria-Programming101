def prime_factorization(n):
    i = 2 
    count = 0
    tuples = []
    while n > 1 and i <= n:
        if is_prime(i) and n % i == 0:
            count = 0
            while n > 1 and n % i == 0:
                n = n/i
                count += 1
            tuples.append((i,count))
        else:
            i += 1
    return tuples

def sum_of_divisors(n):
    if n < 0:
        n = abs(n)
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum = sum + i
    return sum

def is_prime(n):
    if sum_of_divisors(n) == abs(n) + 1:
        return True
    else: 
        return False