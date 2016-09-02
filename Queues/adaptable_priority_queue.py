"""python implementation of Adaptable Priority Queue"""

from Queues.heap_priority_queue import HeapPriorityQueue

class AdaptablePriorityQueue(HeapPriorityQueue):
    """
    a heap priority queue using locators
    so elements can be updated or deleted
    """

    class Locator(HeapPriorityQueue._Item):
        """
        token for locating an entry
        """
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def add(self, key, value):
        """
        add key value pair O(logn)
        """
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, new_key, new_value):
        """
        update key and value for entry identified by Locator loc O(logn)
        """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("invalid locator")
        loc._key = new_key
        loc._value = new_value
        self._bubble(j)

    def remove(self, loc):
        """
        return and remove key value pair identified by Locator loc O(logn)
        """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("invalid locator")
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)




    def _swap(self, i, j):
        """
        override to swap record indices
        """
        super._swap()
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
