"""python implementation of ADT Queue using a Linked List"""

from Queues._queue_abstract import Queue

class LinkedQueue(Queue):
    """
    implementing ADT Queue with a singly linked list
    """

    class Node:
        """
        node for singly linked list
        """
        __slots__ = 'value', 'next'

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        head = self.head
        while head is not None:
            yield head.value
            head = head.next

    def __repr__(self):
        if self.head is None:
            return 'LinkedQueue: []'
        return 'LinkedQueue: [{0:s}]'.format(', '.join(map(str, self)))

    def is_empty(self):
        """
        check if Queue is empty O(1)
        """
        return self.size == 0

    def peek(self):
        """
        return element at front of Queue O(1)
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.head.value

    def dequeue(self):
        """
        remove element at front of Queue O(1)
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def enqueue(self, value):
        """
        add element to back of Queue O(1)
        """
        new = self.Node(value, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1
