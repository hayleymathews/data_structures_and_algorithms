"""example using sorted map to maintain a maxima set"""

from Hashes.sorted_table_map import SortedTableMap

class CostPerformanceDatabase:
    """
    maintains a database of maximal cost-performance pairs
    """

    def __init__(self):
        self._M = SortedTableMap()

    def best(self, c):
        """
        return cost-performance pair with largest cost not exceeding c O(logn)
        """
        self._M.find_less(c)

    def add(self, c, p):
        """
        add new entry with cost c and performance p O(n)
        """
        other = self._M.find_less(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_greater(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_greater(c)
