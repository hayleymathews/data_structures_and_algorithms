"""example using Deque to check is string is a palindrome"""
from Deques.linked_deque import LinkedDeque

def palindrome_checker(string):
    """
    checks if string is a palindrome
    >>> palindrome_checker('a man a plan a canal panama')
    True
    >>> palindrome_checker('moon')
    False
    """
    deque = LinkedDeque()

    for character in string.replace(" ", ""):
        deque.insert_first(character)

    equal = True

    while len(deque) > 1 and equal:
        first = deque.delete_first()
        last = deque.delete_last()
        if first != last:
            equal = False
    return equal
