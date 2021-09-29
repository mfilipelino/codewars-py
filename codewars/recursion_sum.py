def recursion_add(n):
    if n == 0:
        return 0
    else:
        return n + recursion_add(n - 1)
