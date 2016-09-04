"""python implementation of Insertion Sort with Positional List
>>> p = PositionalList()
>>> p.add_first(1)
Position: 1
>>> p.add_first(3)
Position: 3
>>> p.add_first(2)
Position: 2
>>> insertion_sort(p)
PositionalList: [1, 2, 3]
"""

from Lists.positional_list import PositionalList
def insertion_sort(List):
    if len(List) > 1:
        marker = List.first()
        while marker != List.last():
            pivot = List.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != List.first() and List.before(walk).element() > value:
                    walk = List.before(walk)
                List.delete(pivot)
                List.add_before(walk, value)
    return List
