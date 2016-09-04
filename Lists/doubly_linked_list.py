"""python implementation of ADT Doubly Linked List"""

from Lists._list_abstract import List

class DoublyLinkedList(List):
    """
    implementing Doubly Linked List
    """
    class Node:
        """
        node for doubly linked list
        """
        __slots__ = 'value', 'prev', 'next'

        def __init__(self, value, prev, next):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, *start):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        for _ in start:
            self.prepend(_)

    def __len__(self):
        """
        return length of list O(1)
        """
        return self.size

    def __iter__(self):
        head = self.header.next
        while head is not self.trailer:
            yield head.value
            head = head.next

    def __repr__(self):
        if self.header.next is None:
            return 'DoublyLinkedList: []'
        return 'DoublyLinkedList: [{0:s}]'.format(', '.join(map(str, self)))

    def is_empty(self):
        """
        check if list is empty O(1)
        """
        return self.size == 0

    def prepend(self, value):
        """
        add element to front of list O(1)
        """
        new_node = self.Node(value, self.header, self.header.next)
        self.header.next = new_node
        new_node.next.prev = new_node
        self.size += 1

    def append(self, value):
        """
        add element to end of list O(1)
        """
        new_node = self.Node(value, self.trailer.prev, self.trailer)
        self.trailer.prev = new_node
        new_node.prev.next = new_node
        self.size += 1

    def delete_first(self):
        """
        delete element at front of list O(1)
        """
        self.header.next = self.header.next.next.next
        self.header.next.next.prev = self.header.next
        self.size -= 1

    def delete_last(self):
        """
        delete element at end of list O(1)
        """
        self.trailer.prev = self.trailer.prev.prev.prev
        self.trailer.prev.prev.next = self.trailer.prev
        self.size -= 1


    def insert_between(self, value, predecessor, successor):
        """
        add element between two existing nodes and return new node O(1)
        """
        new = self.Node(value, predecessor, successor)
        predecessor.next = new
        successor.prev = new
        self.size += 1
        return new

    def delete_node(self, node):
        """
        delete nonsentinel node from list and return it O(n)
        """
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        answer = node.value
        node.prev = node.next = node.value = None
        return answer
