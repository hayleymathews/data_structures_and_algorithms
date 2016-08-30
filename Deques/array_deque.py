"""python implementation of ADT Deque
with python list (which is really a dynamic array)"""

from Deques.deque_abstract import Deque

class ArrayDeque(Deque):
    """
    implementing ADT Deque
    """
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for item in self.items:
            yield item

    def __repr__(self):
        if self.is_empty():
            return 'ArrayDeque: []'
        return 'ArrayDeque: [{0:s}]'.format(', '.join(map(str, self)))

    def is_empty(self):
        """
        check if Deque is empty O(1)
        """
        return self.items == []

    def insert_first(self, item):
        """
        add item to front of Deque O(n)
        """
        self.items.insert(0, item)

    def insert_last(self, item):
        """
        add item to back of Deque O(1)
        """
        self.items.append(item)

    def delete_first(self):
        """
        remove item from front of Deque O(n)
        """
        return self.items.pop(0)

    def delete_last(self):
        """
        remove item from back of Deque O(1)
        """
        return self.items.pop()
