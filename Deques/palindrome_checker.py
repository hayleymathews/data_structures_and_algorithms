"""example using Deque to check is string is a palindrome"""
from deque import Deque

def palindrome_checker(string):
    """
    checks if string is a palindrome
    >>> palindrome_checker('a man a plan a canal panama')
    True
    >>> palindrome_checker('moon')
    False
    """
    deque = Deque()

    for character in string.replace(" ", ""):
        deque.add_front(character)

    equal = True

    while len(deque) > 1 and equal:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            equal = False
    return equal
