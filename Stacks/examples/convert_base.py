""" convert base of number """

from Stacks.array_stack import ArrayStack

def convert_base(number, base):
    """
    convert number to base O(log n)
    >>> convert_base(266, 16)
    '10A'
    """
    digits = "0123456789ABCDEF"

    stack = ArrayStack()

    while number > 0:
        remainder = number % base
        stack.push(remainder)
        number = number // base

    string = ""
    while not stack.is_empty():
        string = string + digits[stack.pop()]
    return string
