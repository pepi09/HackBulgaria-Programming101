def simplify_fraction(fraction):
    a = gcd(fraction[0],fraction[1])
    return (fraction[0]/a,fraction[1]/a)

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x