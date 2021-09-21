from codewars.linkedlist import SinglyLinkedList, insertNodeAtPosition, print_singly_linked_list


def test_insert_node_at_position():
    llist = SinglyLinkedList()
    for i in [1, 2, 3]:
        llist.insert_node(i)
    head = insertNodeAtPosition(llist.head, 4, 2)
    print_singly_linked_list(head)

