from codewars.queue.queue_with_stack import NewQueue


def test_enqueue():
    queue = NewQueue()
    print()
    [queue.enqueue(i) for i in range(10)]
    print(queue.main_stack.stack_list)
    assert queue.dequeue() == 0
    print(queue.main_stack.stack_list)
    assert queue.dequeue() == 1
    print(queue.main_stack.stack_list)
    queue.enqueue(1)
    print(queue.main_stack.stack_list)
    queue
