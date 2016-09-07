"""example using Stack to find the max span in array of values where value has been increasing
example: max number of consecutive days the price of a stock
has been less than or equal to its price on day index"""

from Stacks.linked_stack import LinkedStack

def find_max_span(values):
    """
    find max span of same or increasing O(n)
    >>> find_max_span([6, 3, 4, 5, 2])
    [1, 1, 2, 3, 1]
    """
    stack = LinkedStack()
    span = [None] * len(values)
    for index, value in enumerate(values):
        while not stack.is_empty() and value > values[stack.peek()]:
            stack.pop()
        if stack.is_empty():
            previous = -1
        else:
            previous = stack.peek()
        span[index] = index - previous
        stack.push(index)
    return span
