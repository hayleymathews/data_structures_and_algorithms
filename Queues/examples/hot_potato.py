"""play hot potato game with Queue"""

from Queues.array_queue import ArrayQueue

def hot_potato(names, number):
    """
    cycle around Queue playing hot potato
    >>> hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
    'Susan'
    """
    queue = ArrayQueue()
    for name in names:
        queue.enqueue(name)
    while len(queue) > 1:
        for _ in range(number):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()
