"""python implementation of ADT static array"""

import ctypes
from Arrays.array_abstract import Array

class StaticArray(Array):
    """
    implementing ADT Array
    """
    def __init__(self, size):
        self.size = size
        self.values = (size * ctypes.py_object)(*([None] * size))

    def __len__(self):
        """
        length of Array O(1)
        """
        return self.size

    def __iter__(self):
        for item in self.values:
            yield item

    def __repr__(self):
        return 'StaticArray: [{0:s}]'.format(', '.join(map(str, self)))

    def __getitem__(self, index):
        """
        get item from Array O(1)
        """
        if not 0 <= index < self.size:
            raise IndexError('invalid index')
        return self.values[index]

    def __setitem__(self, index, value):
        """
        set item in Array O(1)
        """
        if not 0 <= index < self.size:
            raise IndexError('invalid index')
        else:
            self.values[index] = value
