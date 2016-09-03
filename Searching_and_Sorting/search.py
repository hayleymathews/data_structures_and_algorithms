"""python implementation of basic search algorithms
linear search and binary search, """

import collections

class Search:
    """
    various searches
    """

    def linear_search(values, target):
        """
        iterate through input values looking for target O(n)
        note: the pythonic way to do linear search is to use 'in' operator
        """
        try:
            for value in values:
                if value == target:
                    return True
            return False
        except TypeError:
            print("input is not iterable")

    def sorted_linear_search(values, target):
        """
        iterate through presorted input values looking for target O(n)
        if value larger than target, break
        """
        # assert iterable, "input is not iterable"
        for value in values:
            if value == target:
                return True
            elif value > target:
                return False

    def binary_search(values, target):
        """
        iterate through presorted input values looking for target O(logn)
        """
        start = 0
        end = len(values) - 1
        while low <= high:
            mid_point = (high + low) // 2
            if values[mid_point] == target:
                return True
            elif target < values[mid_point]:
                high = mid_point - 1
            else:
                low = mid_point + 1
        return False
