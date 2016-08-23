"""python implementation of ADT Stack using a Linked List"""

class LinkedStack:
    """
    implementing ADT Stack using a singly linked list
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
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        """
        check if stack is empty O(1)
        """
        return self.size == 0

    def push(self, value):
        """
        add to top of stack O(1)
        """
        self.head = self.Node(value, self.head)
        self.size += 1

    def peek(self):
        """
        return top item in stack O(1)
        """
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.value

    def pop(self):
        """
        remove and return top item in stack O(1)
        """
        if self.is_empty():
            raise Exception("Empty list")
        answer = self.head.value
        self.head = self.head.next
        self.size -= 1
        return answer
