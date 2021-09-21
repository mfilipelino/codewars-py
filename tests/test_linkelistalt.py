from codewars.linkelistalt import LinkedList, Node, rotate_list


def test_print_all():
    linked_list = LinkedList()
    for i in range(1, 6, 1):
        linked_list.add(Node(i))
    linked_list.print_all()
    rotate_list(linked_list, 2)
    linked_list.print_all()


def test_print_all_2():
    linked_list = LinkedList()
    for i in range(1, 6, 1):
        linked_list.add(Node(i))
    linked_list.print_all()
    rotate_list(linked_list, -2)
    linked_list.print_all()
