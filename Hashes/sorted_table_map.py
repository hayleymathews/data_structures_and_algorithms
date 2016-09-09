"""python implementation of ADT Map using an sorted list"""

from Hashes._map_abstract import Map

class SortedTableMap(Map):
    """
    implementing a map with a sorted list
    """

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        """
        return value associated with key k O(logn)
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """
        assign value v to key k, overwriting if present O(n) or O(logn) if key already exists
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value == v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        """
        remove item associated with key k O(n)
        """
        j = self._find_index(k, 0, len(self._table) -1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)

    def __iter__(self):
        """
        iterate through keys in map O(n)
        """
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """
        generate keys of map ordered from max to min O(n)
        """
        for item in reversed(self._table):
            yield item._key

    def __contains__(self, k):
        """
        check if key k in map O(logn)
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
        if len(self) == 0:
            return "SortedTableMap: "
        args = ['{}: {}'.format(k, repr(v)) for (k,v) in self.items()]
        return 'SortedTableMap: {{{}}}'.format(', '.join(args))

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

    def clear(self):
        """
        remove all key-value pairs from map O(n)
        """
        for item in self._table:
            del self[item._key]

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

    def find_min(self):
        """
        return key-value pair with minimum key O(1)
        """
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """
        return key-value pair with maximum key O(1)
        """
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_greater_or_equal(self, k):
        """
        return key-value pair with least key greater than or equal to k O(logn)
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_less(self, k):
        """
        return key-value pair with greatest key less than k O(logn)
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def find_greater(self, k):
        """
        return key-value pair with least key greater than k O(logn)
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j + 1]._key, self._table[j + 1]._value)
        else:
            return None

    def find_range(self, start, stop):
        """
        return all key-value pairs with key between start and stop O(s + logn)
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1

    def _find_index(self, k, low, high):
        """
        add the description dummy O(logn)
        """
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid+ 1, high)
