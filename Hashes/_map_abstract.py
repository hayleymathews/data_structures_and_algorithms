"""abstract class for ADT Map

note:
this is pretty much the same thing as collections.abc MutableMapping
replicated here just to show the expected behaviors for a map"""

from abc import ABC, abstractmethod

class Map(ABC):
    """
    abstract class representing map structure
    """
    class _Item:
        """
        lightweight composite to store key-value pairs
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not self == other

        def __lt__(self, other):
            return self._key < other._key

    @abstractmethod
    def __getitem__(self, k):
        """
        return value v associated with key k
        """
        pass

    @abstractmethod
    def __setitem__(self, k, v):
        """
        associate value v with key k, replacing existing value
        """
        pass

    @abstractmethod
    def __delitem__(self, k):
        """
        remove from map item with key k
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        return number of items in map
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        iterate through items in map
        """
        pass

    @abstractmethod
    def __contains__(self, k):
        """
        return True if map contains an item with key k
        """
        pass

    @abstractmethod
    def __eq__(self, other_map):
        """
        return True if map and other_map have identical key-value pairs
        """
        pass

    @abstractmethod
    def __ne__(self, other_map):
        """
        return True if map and other_map don't have identical key-value pairs
        """
        pass

    @abstractmethod
    def get(self, k, d=None):
        """
        return value for key k if exists,
        otherwise return default d
        """
        pass

    @abstractmethod
    def setdefault(self, k, d):
        """
        if key k exists return value for k
        else set k's value to default d
        """
        pass

    @abstractmethod
    def pop(self, k, d=None):
        """
        remove and return item associated with key k,
        if k doesn't exist, return default d
        """
        pass

    @abstractmethod
    def popitem(self):
        """
        remove and return arbitrary item
        """
        pass

    @abstractmethod
    def clear(self):
        """
        remove all key-value pairs from map
        """
        pass

    @abstractmethod
    def keys(self):
        """
        return a set of all keys
        """
        pass

    @abstractmethod
    def values(self):
        """
        return a set of all values
        """

    @abstractmethod
    def items(self):
        """
        return a set of all key-value pairs
        """
        pass

    @abstractmethod
    def update(self, other_map):
        """
        assign map[k] = v for every k, v pair in other_map
        """
        pass
