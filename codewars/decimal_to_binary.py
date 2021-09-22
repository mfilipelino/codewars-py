def decimal_to_binary(n):
    if n == 1:
        return "1"
    if n == 0:
        return "0"

    return decimal_to_binary(n // 2) + str(n % 2)
