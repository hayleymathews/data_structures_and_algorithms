"""python implementation of ADT Queue
with python list (which is really a dynamic array)"""

class Queue:
    """
    implementing ADT Queue
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return "Queue: " + str(self.items)

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        """
        check if Queue empty O(1)
        """
        return self.items == []

    def enqueue(self, item):
        """
        add item to bottom of Queue O(n)
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        remove item from top of Queue O(1)
        """
        return self.items.pop()
