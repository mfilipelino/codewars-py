from codewars.reverse_k import MyStack, MyQueue


def test_reverse_k():
    queue = MyQueue()
    stack = MyStack()
    [queue.enqueue(i) for i in range(1, 11, 1)]
    print()
    print(queue.queue_list)
    for i in range(0, 5, 1):
        value = queue.dequeue()
        stack.push(value)
    print(queue.queue_list)
    print(stack.stack_list)
    new_queue = MyQueue()
    while not stack.is_empty():
        new_queue.enqueue(stack.pop())

    while not queue.is_empty():
        new_queue.enqueue(queue.dequeue())
    print(new_queue.queue_list)
