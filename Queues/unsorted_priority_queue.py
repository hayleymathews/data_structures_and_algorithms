"""python implementation of ADT Priority Queue with an unsorted list"""

from Queues.priority_queue_abstract import PriorityQueue
from Lists.positional_list import PositionalList

class UnsortedPriorityQueue(PriorityQueue):
    """
    implementing unsorted priority queue
    """

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """
        add element to queue O(1)
        """
        self._data.add_last(self._Item(key, value))

    def min(self):
        """
        return item with minimum key O(n)
        """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        remove and return item with minimum key O(n)
        """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

    def _find_min(self):
        """
        return position of item with minimum key O(n)
        """
        if self.is_empty():
            raise Exception("priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small    
