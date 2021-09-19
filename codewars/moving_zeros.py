def move_zeros(array):
    result = []
    for a in reversed(array):
        if a == 0:
            result.append(a)
        else:
            result.insert(0, a)
    return result


def fatorial(n):
    return 1 if n <= 1 else fatorial(n - 1) * n