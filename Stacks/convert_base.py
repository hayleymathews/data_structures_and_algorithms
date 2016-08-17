""" convert base of number """

from stack import Stack

def convert_base(number, base):
    """
    convert number to base O(log n)
    >>> convert_base(266, 16)
    '10A'
    """
    digits = "0123456789ABCDEF"

    stack = Stack()

    while number > 0:
        remainder = number % base
        stack.push(remainder)
        number = number // base

    string = ""
    while not stack.is_empty():
        string = string + digits[stack.pop()]
    return string
