from codewars.linkedlist_operations import union, intersection, find_nth
from codewars.linkedlist import LinkedList


def test_union():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert_at_tail(1)
    l1.insert_at_tail(2)
    l1.insert_at_tail(3)
    l2.insert_at_tail(3)
    l2.insert_at_tail(4)
    l2.insert_at_tail(5)
    l3 = union(l1, l2)
    l3.print_list()


def test_intersection():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert_at_tail(1)
    l1.insert_at_tail(2)
    l1.insert_at_tail(3)
    l2.insert_at_tail(3)
    l2.insert_at_tail(4)
    l2.insert_at_tail(5)
    l3 = intersection(l1, l2)
    l3.print_list()


def test_find_nth():
    l1 = LinkedList()
    for i in range(10):
        l1.insert_at_tail(i)

    print(find_nth(l1, 4))
