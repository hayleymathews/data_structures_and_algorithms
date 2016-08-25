"""improving move to front for FavoritesList"""

from Lists.favorites_list import FavoritesList
from Lists.positional_list import PositionalList

class FavoritesListMTF(FavoritesList):
    """
    list of elements ordered with move-to-front heuristic
    """
    def _move_up(self, p):
        """
        move accessed item at Position p to front of list
        """
        if p != self.data.first():
            self.data.add_first(self.data.delete(p))

    def top(self, k):
        """
        generate sequence of top k elements in terms of access
        """
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        temp = PositionalList()
        for item in self.data:
            temp.add_last(item)

        for j in range(k):
            high_pos = temp.first()
            walk = temp.after(high_pos)
            while walk is not None:
                if walk.element()._count > high_pos.element()._count:
                    high_pos = walk
                walk = temp.after(walk)
            yield high_pos.element()._value
            temp.delete(high_pos)
