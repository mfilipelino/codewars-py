class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def add(self, node):
        self.size += 1
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def print_all(self):
        node = self.head
        print()
        while node.next is not None:
            print(str(node), end=" ")
            node = node.next
        print(str(node), end=" ")
        print()



def rotate_list(lst, k):

    k = k + 1 if k > 0 else -1 * k
    lst.tail.next = lst.head
    for i in range(0, k):
        lst.head = lst.head.next
        lst.tail = lst.tail.next
    lst.tail.next = None
