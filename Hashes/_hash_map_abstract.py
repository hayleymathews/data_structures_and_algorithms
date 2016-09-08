"""abstract class for ADT Hash Map
hasing allows for faster retrieval and updates"""

from abc import ABC, abstractmethod
from random import randrange
from Hashes._map_abstract import Map

class HashMap(Map, ABC):
    """
    abstract class representing a map with hashing
    """

    def __init__(self, cap=11, p=109345121):
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        """
        hashes key k to a bucket
        """
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        """
        hash key k to bucket j and find item in j associated with k
        """
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        """
        hash key k to bucket j and create new or overwrite value of k to v
        resize bucket array if necessary
        """
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) -1)

    def __delitem__(self, k):
        """
        hash k to bucket j and delete item in j associated with k
        """
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def __contains__(self, k):
        try:
            self[k]
            return True
        except KeyError:
            return False

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def clear(self):
        """
        remove all key-value pairs from map O(n)
        """
        for key in self.keys():
            del self[key]

    def get(self, k, d=None):
        """
        return value v for key k if exists, else return default d O(n)
        """
        try:
            return self[k]
        except KeyError:
            return d

    def items(self):
        """
        return all key-value pairs in map O(n)
        """
        return list(zip(self.keys(), self.values()))

    def keys(self):
        """
        return all keys in map O(n)
        """
        return list(self.__iter__())

    def values(self):
        """
        return all values in map O(n)
        """
        values = []
        for key in self.keys():
            values.append(self[key])
        return values

    def pop(self, k, d=None):
        """
        remove and return item with key k if exists, else return d O(n)
        """
        try:
            answer = self[k]
            del self[k]
            return answer
        except KeyError:
            return d

    def popitem(self):
        """
        remove and return arbitrary item from map O(1)
        """
        pass

    def setdefault(self, k, d):
        """
        return value v for key k if exists, else set value of k to d O(n)
        """
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d

    def _resize(self, c):
        """
        resize bucket array to capacity c
        """
        old = list(self.items())
        self._table = [None] * c
        self._n = 0
        for (k, v) in old:
            self[k] = v

    @abstractmethod
    def __iter__(self):
        """
        iterate through all keys of map
        """
        pass

    @abstractmethod
    def _bucket_getitem(self, j, k):
        """
        search bucket j for an item with key k and return or raise KeyError
        """
        pass

    @abstractmethod
    def _bucket_setitem(self, j, k, v):
        """
        modify bucket j so key k is associated with value v
        creates new or overwrites
        """
        pass

    @abstractmethod
    def _bucket_delitem(self, j, k):
        """
        remove item from bucket j having key k or raise KeyError
        """
        pass
