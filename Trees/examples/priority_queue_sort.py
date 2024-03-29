"""sort a collection of elements stored in a positional list"""

from Lists.positional_list import PositionalList
from Queues.heap_priority_queue import HeapPriorityQueue

def pq_sort(C):
    assert type(C) is PositionalList, "input is not a positional list"
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)    
