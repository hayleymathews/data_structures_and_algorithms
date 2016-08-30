"""example with Positional List, making a list of favorites"""

from Lists.examples.positional_list import PositionalList

class FavoritesList:
    """
    list of elements ordered from most frequently accessed to least
    """
    class _Item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        """
        search for element e and return its Position
        """
        walk = self.data.first()
        while walk is not None and walk.element()._value != e:
            walk = self.data.after(walk)
        return walk

    def _move_up(self, p):
        """
        move item at Position p earlier in list based on access count
        """
        if p != self.data.first():
            count = p.value()._count
            walk = self.data.before(p)
            if count > walk.element()._count:
                while (walk != self.data.first() and
                       count > self.data.before(walk).element()._count):
                    walk = self.data.before(walk)
                self.data.add_before(walk, self.data.delete(p))

    def __init__(self):
        self.data = PositionalList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def access(self, e):
        """
        access element e, thereby incresing its access count
        """
        p = self._find_position(e)
        if p is None:
            p = self.data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """
        remove element e from list
        """
        p = self._find_position(e)
        if p is not None:
            self.data.delete(p)

    def top(self, k):
        """
        get sequence of top k elements
        """
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self.data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self.data.after(walk)
