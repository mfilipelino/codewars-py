def reverse_stack(stack, new_stack = []):
    if len(stack) == 0:
        return
    else:
        e = stack.pop()
        new_stack = reverse_stack(stack)
        stack.append(e)
        return stack

"""
"""


n = 10  # can be anything, this is just an example
sum = 0
pie = 3.14                           # 3
for var in range(1, n, 3):           # 1, 3, 6 ... n         n + 1 / 3
    j = 1
    print(pie)                       # 3
    while j < n:                     #
        sum += 1
        j *= 3
print(sum)  # O(1)