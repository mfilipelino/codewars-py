def calc(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "/":
        return a / b
    else:
        return a * b


def stack_exaluate_post_fix(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        stack = []
        while lst != []:
            element = lst.pop(0)
            if element in "+-*/":
                a = stack.pop()
                b = stack.pop()
                stack.append(calc(element, b, a))

            else:
                stack.append(int(element))
        return stack.pop()


def evaluate_post_fix(exp):
    return stack_exaluate_post_fix(list(exp))
