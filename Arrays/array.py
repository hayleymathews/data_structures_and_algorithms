"""python implementation of ADT array"""
import ctypes

class Array:
    def __init__(self, size):
        self.size = size
        self.values = (size * ctypes.py_object)()

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value
