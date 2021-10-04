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


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here

    # Inserts Element in the Queue
    def enqueue(self, value):
        self.main_stack.push(value)

    # Removes Element From Queue
    def dequeue(self):
        if self.main_stack.is_empty():
            return None
        elif self.main_stack.size() == 1:
            return self.main_stack.pop()
        else:
            top = self.main_stack.pop()
            value = self.dequeue()
            self.main_stack.push(top)
            return value

    """
    dequeue(stack = [1, 2, 3]) | top = 3 | value =  1   | stack= [2, 3]
    dequeue(stack = [1, 2])    | top = 2 | value =  1   | stack = [2]
    dequeue(stack = [1])       |         | value =  1   | stack = []
    """
