def perimeter(n):
    a, b = 1, 1
    s = a + b
    if n > 2:
        for i in range(3, n + 2, 1):
            next = a + b
            a = b
            b = next
            s += next
    return s * 4
