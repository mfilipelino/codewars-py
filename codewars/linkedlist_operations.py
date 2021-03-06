from codewars.linkedlist import LinkedList


def union(list1, list2):
    list3 = LinkedList()

    node = list1.get_head()
    while node is not None:
        list3.insert_at_tail(node.data)
        node = node.next_element

    node = list2.get_head()
    while node is not None:
        list3.insert_at_tail(node.data)
        node = node.next_element

    list3.remove_duplicates()

    return list3


# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    list3 = LinkedList()
    hashmap = dict()

    node = list1.get_head()
    while node is not None:
        hashmap[node.data] = True
        node = node.next_element

    node = list2.get_head()
    while node is not None:
        if node.data in hashmap:
            list3.insert_at_tail(node.data)
        node = node.next_element

    return list3


def find_nth(lst, n):
    node = lst.get_head()
    size = lst.length()
    index = 0
    for _ in range(0, size - n, 1):
        node = node.next_element
    return node.data
