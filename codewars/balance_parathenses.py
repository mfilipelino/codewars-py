class Stack:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    def top(self):
        if self.is_empty() is False:
            return self.lst[-1]
        else:
            return None

    def append(self, value):
        self.lst.append(value)

    def pop(self):
        self.lst.pop()


def balanced(s):
    stack = Stack()
    for c in s:
        if c == ")" and stack.is_empty():
            return False
        elif c == ")" and stack.top() == "(":
            stack.pop()
        elif c == "(":
            stack.append("(")
    return stack.is_empty()


def recursive_balanced(s, index=0, open=0):

    if index == len(s):
        return open == 0

    if open < 0:
        return False

    if s[index] == "(":
        return recursive_balanced(s, index + 1, open + 1)
    else:
        return recursive_balanced(s, index + 1, open - 1)
