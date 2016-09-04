"""python implementation of ADT Priority Queue with a heap"""

from Queues._priority_queue_abstract import PriorityQueue

class HeapPriorityQueue(PriorityQueue):
    """
    implementing heapified priority queue
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        """
        get length of heap O(1)
        """
        return len(self._data)

    def add(self, key, value):
        """
        add key value pair to priority queue O(logn)
        """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        """
        return key value with minimum key O(1)
        """
        if self.is_empty():
            raise Exception("priority queue is empty")
        item = self._data[0]
        return(item._key, item._value)

    def remove_min(self):
        """
        return and remove key value with minimum key O(logn)
        """
        if self.is_empty():
            raise Exception("priority queue is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return(item._key, item._value)

    def _parent(self, j):
        """
        get parent of node j O(1)
        """
        return (j - 1) // 2

    def _left(self, j):
        """
        get left child of node j O(1)
        """
        return 2*j + 1

    def _right(self, j):
        """
        get right child of node j O(1)
        """
        return 2*j + 2

    def _has_left(self, j):
        """
        check if j has left child O(1)
        """
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        """
        check if j has right child O(1)
        """
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """
        swap elements at indices i and j of array
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """
        move j up heap
        """
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        """
        move j down heap
        """
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
                if self._data[small_child] < self._data(j):
                    self._swap(j, small_child)
                    self._downheap(small_child)
