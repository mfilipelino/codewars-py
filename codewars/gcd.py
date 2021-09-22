def gcd(a, b):
    if a < 1 or b < 1:
        return 1
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
