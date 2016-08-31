"""python implementation of ADT Priority Queue with a sorted list"""

from Queues.priority_queue_abstract import PriorityQueue
from Lists.positional_list import PositionalList

class SortedPriorityQueue(PriorityQueue):
    """
    implementing sorted priority queue
    """

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """
        add key-value pair to list O(n)
        """
        new = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)
        else:
            self._data.add_after(walk, new)

    def min(self):
        """
        return item with minimum key O(1)
        """
        if self.is_empty():
            raise Exception("priority queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        remove and return item with minimum key O(1)
        """
        if self.is_empty():
            raise Exception("priority queue is empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
