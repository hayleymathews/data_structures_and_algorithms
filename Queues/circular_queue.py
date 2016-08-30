"""python implementation of a circular Queue for round robin
scheduling using circularly linked list"""

from Queues.queue_abstract import Queue

class CircularQueue(Queue):
    """
    implementing a Queue using a circularly linked list
    """
    class Node:
        """
        node for circularly linked list
        """
        __slots__ = 'value', 'next'

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

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
            raise Exception("Queue is empty")
        head = self.tail.next
        return head.value

    def dequeue(self):
        """
        return and remove element at front of Queue O(1)
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = answer.next
        self.size -= 1
        return answer.value

    def enqueue(self, value):
        """
        add element to back of Queue O(1)
        """
        new = self.Node(value, None)
        if self.is_empty():
            new.next = new
        else:
            new.next = self.tail.next
            self.tail.next = new
        self.tail = new
        self.size += 1

    def rotate(self):
        """
        rotate front element to back of Queue O(1)
        """
        if self.size > 0:
            self.tail = self.tail.next
