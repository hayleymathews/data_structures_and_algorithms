"""abstract class for ADT Priority Queue"""

from abc import ABC, abstractmethod

class PriorityQueue(ABC):
    """
    abstract class representing Queue
    """

    class _Item:
        """
        store priority queue items
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        """
        check if priority queue is empty
        """
        return len(self) == 0

    @abstractmethod
    def __len__(self):
        """
        get length of priority Queue
        """
        pass

    @abstractmethod
    def add(self, k, v):
        """
        insert item with key k and value v
        """
        pass

    @abstractmethod
    def min(self):
        """
        return tuple of key and value of item with smallest key
        """
        pass

    @abstractmethod
    def remove_min(self):
        """
        remove and return tuple of key and value of item with smallest key
        """
        pass
