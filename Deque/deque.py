"""python implementation of ADT Deque
with python list (which is really a dynamic array)"""

class Deque():
    """
    implementing ADT Deque
    """
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        """
        check if Deque is empty O(1)
        """
        return self.items == []

    def add_front(self, item):
        """
        add item to top of Deque O(1)
        """
        self.items.append(item)

    def add_rear(self, item):
        """
        add item to bottom of Deque O(n)
        """
        self.items.insert(0, item)

    def remove_front(self):
        """
        remove item from top of Deque O(1)
        """
        return self.items.pop()

    def remove_rear(self):
        """
        remove item from bottom of Deque O(n)
        """
        return self.items.pop(0)
