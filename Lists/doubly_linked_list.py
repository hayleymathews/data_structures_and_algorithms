"""python implementation of ADT Doubly Linked List"""

class DoublyLinkedList:
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

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        """
        check if list is empty O(1)
        """
        return self.size == 0

    def insert_between(self, value, predecessor, successor):
        """
        add element between two existing nodes and return new node
        """
        new = self.Node(value, predecessor, successor)
        predecessor.next = new
        successor.prev = new
        self.size += 1
        return new

    def delete_node(self, node):
        """
        delete nonsentinel node from list and return it
        """
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = prev
        self.size -= 1
        answer = node.value
        node.prev = node.next = node.value = None
        return answer
        
