def numbers_exponencial(num):
    result = []
    while num > 0:
        yield num % 10
        num = num // 10


def find_happy_number(num):
    group = set()
    result = num
    while True:
        result = sum([int(c) ** 2 for c in numbers_exponencial(num)])
        if result == 1:
            return f"true ({num} is a happy number)"
        if result in group:
            return f"false ({num} is not a happy number)"
        group.add(result)
