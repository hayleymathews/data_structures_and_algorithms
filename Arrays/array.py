"""python implementation of ADT array"""
import ctypes

class Array:
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

    def __getitem__(self, index):
        """
        get item from Array O(1)
        """
        return self.values[index]

    def __setitem__(self, index, value):
        """
        set item in Array O(1)
        """
        self.values[index] = value
