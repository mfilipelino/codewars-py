def reverse_stack(stack, new_stack=[]):
    if len(stack) == 0:
        return
    else:
        e = stack.pop()
        new_stack = reverse_stack(stack)
        stack.append(e)
        return stack
