"""python implementation of Insertion Sort with Positional List"""

def insertion_sort(List):
    if len(List) > 1:
        marker = List.first()
        while marker != List.last():
            pivot = List.after(marker)
            value = pivot.value()
            if value > marker.value():
                marker = pivot
            else:
                walk = marker
                while walk != List.first() and List.before(walk).value() > value:
                    walk = List.before(walk)
                List.delete(pivot)
                List.add_before(walk, value)    
