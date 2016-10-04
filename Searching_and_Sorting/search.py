"""
python implementation of basic search algorithms
"""

import collections
import random

class Search:
    """
    various searches
    """

    @staticmethod
    def linear_search(values, target):
        """
        iterate through input values looking for target O(n)
        note: the pythonic way to do linear search is to use 'in' operator
        >>> values = [1, 4, 3, 2, 5]
        >>> Search.linear_search(values, 4)
        True
        """
        try:
            for value in values:
                if value == target:
                    return True
            return False
        except TypeError:
            print("input is not iterable")

    @staticmethod
    def sorted_linear_search(values, target):
        """
        iterate through presorted input values looking for target O(n)
        if value larger than target, break
        >>> values = [1, 2, 3, 4, 5]
        >>> Search.sorted_linear_search(values, 4)
        True
        """
        # assert iterable, "input is not iterable"
        for value in values:
            if value == target:
                return True
            elif value > target:
                return False

    @staticmethod
    def binary_search(values, target):
        """
        iterate through presorted input values looking for target O(logn)
        >>> values = [1, 2, 3, 4, 5]
        >>> Search.binary_search(values, 4)
        True
        """
        low = 0
        high = len(values) - 1
        while low <= high:
            mid_point = (high + low) // 2
            if values[mid_point] == target:
                return True
            elif target < values[mid_point]:
                high = mid_point - 1
            else:
                low = mid_point + 1
        return False

    @staticmethod
    def quick_select(values, k):
        """
        find kth smallest item in values O(n)
        >>> values = [1, 4, 3, 2, 5]
        >>> Search.quick_select(values, 2)
        2
        """
        if len(values) == 1:
            return values[0]
        pivot = random.choice(values)
        smaller = [x for x in values if x < pivot]
        larger = [x for x in values if x > pivot]
        equal = [x for x in values if x == pivot]
        if k <= len(smaller):
            return Search.quick_select(smaller, k)
        elif k <= len(smaller) + len(equal):
            return pivot
        else:
            j = k - len(smaller) - len(equal)
            return Search.quick_select(larger, j)
