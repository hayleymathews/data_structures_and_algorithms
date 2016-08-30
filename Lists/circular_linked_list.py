"""python implementation of ADT Circular Linked List"""

from Lists.list_abstract import List

class CircularLinkedList(List):
    """
    implementing Circular Linked List
    """
    class Node:
        """
        node for circular linked list
        """
        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self, *start):
        self.head = self.Node(None, None)
        self.size = 0
        for _ in start:
            self.prepend(_)

    def __len__(self):
        """
        return length of list O(1)
        """
        return self.size

    def __iter__(self):
        """
        TODO: unfuck this up
        """
        if self.size == 0:
            return None
        if self.size < 2:
            yield self.head.value
        else:
            current = self.head
            for x in range(self.size):
                yield current.value
                current = current.next

    def __repr__(self):
        if self.head is None:
            return 'CircularLinkedList: []'
        return 'CircularLinkedList: [{0:s}]'.format(', '.join(map(str, self)))

    def is_empty(self):
        """
        check if circular linked list is empty O(1)
        """
        return self.size == 0

    def prepend(self, value):
        """
        add element to beginning of list O(n)
        """
        new_node = self.Node(value, None)
        new_node.next = new_node
        if self.head.next is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
        self.size += 1

    def append(self, value):
        """
        add element to end of list O(n)
        TODO: unfuck this up
        """
        new_node = self.Node(value, None)
        if self.head.value is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            previous = self.head
            while current.next is not self.head:
                previous = current
                current = current.next
            new_node.next = self.head
            previous.next = new_node
        self.size += 1

    def delete_first(self):
        """
        remove element at front of list O(1)
        """
        if self.head is None:
            raise Exception("Empty list")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def delete_last(self):
        """
        remove element at back of list O(n)
        """
        if self.head is None:
            raise Exception("Empty list")
        current = self.head
        previous = self.head
        while current.next is not self.head:
            previous = current
            current = current.next
        value = current.value
        previous.next = self.head
        self.size -= 1
        return value
