"""example using Stack to check if parentheses/brackets are balanced in a string"""

from stack import Stack

def parentheses_checker(symbols):
    """
    checks if each opened parentheses/bracket gets closed O(n)
    """
    stack = Stack()
    index = 0
    balanced = True
    while index < len(symbols) and balanced:
        symbol = symbols[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    return bool(balanced and stack.is_empty)

def matches(open, close):
    """
    checks that opening and closing type match O(1)
    """
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)

print(parentheses_checker('{{([][])}()}'))
print(parentheses_checker('[{()]'))
