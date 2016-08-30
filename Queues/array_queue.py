"""python implementation of ADT Queue
with python list (which is really a dynamic array)"""

from Queues.queue_abstract import Queue

class ArrayQueue(Queue):
    """
    implementing ADT Queue
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return "Queue: " + str(self.items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for item in self.items:
            yield item

    def __repr__(self):
        if self.is_empty():
            return 'ArrayQueue: []'
        return 'ArrayQueue: [{0:s}]'.format(', '.join(map(str, self)))

    def is_empty(self):
        """
        check if Queue empty O(1)
        """
        return self.items == []

    def enqueue(self, item):
        """
        add item to bottom of Queue O(1)
        """
        self.items.append(item)

    def dequeue(self):
        """
        remove item from top of Queue O(n)
        """
        return self.items.pop(0)
