"""play hot potato game with Queue"""
from queue import Queue

def hot_potato(names, number):
    """
    cycle around Queue playing hot potato
    >>> hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
    'Susan'
    """
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    while len(queue) > 1:
        for _ in range(number):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()
