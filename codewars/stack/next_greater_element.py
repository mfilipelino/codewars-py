class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()


def next_greater_element(lst):
    n = len(lst)
    stack = MyStack()
    stack.push(-1)
    for i in range(n - 2, -1, -1):
        element = lst[i]
        if element < lst[i + 1]:
            stack.push(lst[i + 1])
        elif element < stack.peek():
            stack.push(stack.peek())
        else:
            stack.push(-1)

    return stack.stack_list[::-1]
