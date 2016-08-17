"""python implementation of ADT Dynamic Array"""

import ctypes

class DynamicArray:
    """
    implementing ADT Dynamic Array
    """
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.values = (self.capacity * ctypes.py_object)(*([None] * self.capacity))

    def __len__(self):
        """
        size of Array O(1)
        """
        return self.size

    def __getitem__(self, index):
        """
        get item from Array O(1)
        """
        if not 0 <= index < self.size:
            raise IndexError('invalid index')
        return self.values[index]

    def append(self, item):
        """
        add item to Array amortized O(1) with resize
        """
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.values[self.size] = item
        self.size += 1

    def resize(self, capacity):
        """
        double size of array when at capacity O(n)
        """
        new_array = (capacity * ctypes.py_object)(*([None] * capacity))
        for i in range(self.size):
            new_array[i] = self.values[i]
        self.values = new_array
        self.capacity = capacity
