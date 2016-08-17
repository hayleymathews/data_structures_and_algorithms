"""python implementation of ADT linked list"""

class Node:
    """
    node to be used in linked list implementation
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    implementing ADT Linked List
    """
    def __init__(self, *start):
        self.head = None
        for _ in start:
            self.prepend(_)

    def __iter__(self):
        head = self.head
        while head is not None:
            yield head.value
            head = head.next

    def __repr__(self):
        if self.head is None:
            return 'LinkedList: []'
        return 'LinkedList: [{0:s}]'.format(', '.join(map(str, self)))

    def prepend(self, value):
        """
        add value to front of linked list O(1)
        """
        self.head = Node(value, self.head)

    def remove(self, value):
        """
        remove specified item from list O(n)
        """
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = self.head.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def pop(self):
        """
        remove first value from list O(1)
        """
        if self.head is None:
            raise Exception("Empty list")
        value = self.head.value
        self.head = self.head.next
        return value
