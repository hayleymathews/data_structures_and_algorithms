"""python implementation of ADT linked list"""

from Lists.list_abstract import List

class LinkedList(List):
    """
    implementing ADT Linked List
    """
    class Node:
        """
        node to be used in linked list implementation
        """
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, *start):
        self.head = None
        self.size = 0
        for _ in start:
            self.prepend(_)

    def __len__(self):
        return self.size

    def __iter__(self):
        head = self.head
        while head is not None:
            yield head.value
            head = head.next

    def __repr__(self):
        if self.head is None:
            return 'LinkedList: []'
        return 'LinkedList: [{0:s}]'.format(', '.join(map(str, self)))

    def is_empty(self):
        """
        check if list is empty O(1)
        """
        return self.size == 0

    def prepend(self, value):
        """
        add value to front of linked list O(1)
        """
        self.head = self.Node(value, self.head)
        self.size += 1

    def append(self, value):
        """
        add value to end of linked list O(n)
        """
        new_node = self.Node(value, None)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size += 1

    def delete_first(self):
        """
        remove value from front list O(1)
        """
        if self.head is None:
            raise Exception("Empty list")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def delete_last(self):
        """
        remove value from end of list O(n)
        """
        if self.head is None:
            raise Exception("Empty list")
        current = self.head
        previous = self.head
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        self.size -= 1

    def insert(self, position, value):
        """
        insert value at position O(n)
        """
        if position > self.size or position < 0:
            raise Exception("invalid position")
        if position == 0:
            self.prepend(value)
        elif position == self.size:
            self.append(value)
        else:
            count = 0
            current = self.head
            while count < position - 1:
                count += 1
                current = current.next
            new_node = self.Node(value, current.next)
            current.next = new_node
            self.size += 1

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

    def reverse(self):
        """
        reverse list O(n)
        """
        last = None
        current = self.head
        while curent is not None:
            next_node = current.next
            current.next = last
            last = current
            current = next
        self.head = last
