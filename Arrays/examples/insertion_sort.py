""" python implementation of Insertion Sort
>>> insertion_sort([3, 2, 1])
[1, 2, 3]
"""

def insertion_sort(array):
    """
    sort an array of comparable elements in ascending order O(n^2)
    """
    for index in range(1, len(array)):
        current = array[index]
        while index > 0 and array[index - 1]> current:
            array[index] = array[index - 1]
            index -= 1
        array[index] = current
    return array
