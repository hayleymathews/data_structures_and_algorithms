"""python implementaton of ADT Deque using Doubly Linked List"""

from Lists.doubly_linked_list import DoublyLinkedList

class LinkedDeque(DoublyLinkedList):
    """
    implementing Dequq with a doubly linked list
    """
    def peek(self):
        """
        return element at front of Deque O(1)
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.header.next.value

    def last(self):
        """
        return element at back of Deque O(1)
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.trailer.prev.value

    def insert_first(self, value):
        """
        add element to front of Deque O(1)
        """
        self.insert_between(value, self.header, self.header.next)

    def insert_last(self, value):
        """
        add element to back of Deque O(1)
        """
        self.insert_between(value, self.trailer.prev, self.trailer)

    def delete_first(self):
        """
        remove and return element from front of Deque O(1)
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        """
        remove and return element from back of Deque O(1)
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.delete_node(self.trailer.prev)
