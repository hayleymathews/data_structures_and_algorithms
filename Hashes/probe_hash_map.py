"""python implementation of map using a hash table with linear probing"""

from Hashes._hash_map_abstract import HashMap

class ProbeHashMap(HashMap):
    """
    implementing hash map with linear probing for collisions
    """

    _AVAIL = object()

    def __repr__(self):
        return "ProbeHashMap: [{}]".format()
                return 'LinkedList: [{0:s}]'.format(', '.join(map(str, self)))



    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def _is_available(self, j):
        """
        return True if index j is available in table
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """
        search for key k in bucket at index j

        return (success, index) tuple
        if match found, success = True, index = location
        if no match found, success = False, index = first available slot
        """
        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j
                if self._table[j] is None:
                    return (False, first_avail)
            elif k == self._table[j]._key:
                return (True, k)
            j = (j + 1) % len(self._table)
