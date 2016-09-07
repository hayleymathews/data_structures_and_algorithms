"""python implementation of ADT Map using an unordered list"""

from Hashes._map_abstract import Map

class UnsortedTableMap(Map):
    """
    implementing a map with unsorted list
    """
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        """
        return value associated with key k O(n)
        """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """
        assign value v to key k, overwriting existing value O(n)
        """
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """
        remove item associated with key k O(n)
        """
        for x in range(len(self._table)):
            if k == self._table[x]._key:
                self._table.pop(x)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """
        return number of items in map O(1)
        """
        return len(self._table)

    def __iter__(self):
        """
        iterate through items in map O(n)
        """
        for item in self._table:
            yield item._key

    def __contains__(self, k):
        """
        check if key k in map O(n)
        """
        try:
            self[k]
            return True
        except KeyError:
            return False

    def __eq__(self, other):
        """
        check if map and other are identical O(n)
        """
        diff = set(self.items()) - set(other.items())
        if diff:
            return False
        return True

    def __ne__(self, other):
        """
        check if map and other are not identical O(n)
        """
        return not (self == other)

    def __repr__(self):
        return 'UnsortedTableMap: [{0:s}]'.format(', '.join(map(str, self)))


    def get(self, k, d=None):
        """
        return value v for key k if exists, else return default d O(n)
        """
        try:
            return self[k]
        except KeyError:
            return d

    def setdefault(self, k, d):
        """
        return value v for key k if exists, else set value of k to d O(n)
        """
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d

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
        item = self._table.pop()
        return (item._key, item._value)

    def clear(self):
        """
        remove all key-value pairs from map O(n)
        """
        for item in self._table:
            del self[item._key]

    def keys(self):
        """
        return all keys in map O(n)
        """
        return [item._key for item in self._table]

    def values(self):
        """
        return all values in map O(n)
        """
        return [item._value for item in self._table]

    def items(self):
        """
        return all key-value pairs in map O(n)
        """
        return [(item._key, item._value) for item in self._table]

    def update(self, other):
        """
        assign map[k] = v for every k, v pair in other
        TODO: figure this one out
        """
        pass
