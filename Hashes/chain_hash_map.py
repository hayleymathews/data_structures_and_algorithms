"""python implementation of map using a hash table with separate chaining"""

from Hashes._hash_map_abstract import HashMap
from Hashes.unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMap):
    """
    implementing hash map with separate chaining for collisions
    """

    def __repr__(self):
        if len(self) == 0:
            return "ChainHashMap: "
        args = ['{}: {}'.format(k, repr(v)) for (k,v) in self.items()]
        return 'ChainHashMap: {{{}}}'.format(', '.join(args))

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]
