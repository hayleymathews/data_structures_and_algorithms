"""
python implementation of basic sort algorithms
"""

import random
import heapq

class Sort:
    """
    various sorts
    """
    @staticmethod
    def bubble_sort(values):
        """
        iterate through values and bubble largest value to end O(n**2)
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.bubble_sort(values)
        [1, 2, 3, 4, 5]
        """
        for a in range(len(values) - 1):
            for b  in range(len(values[:-a])):
                if values[b] > values[b + 1]:
                    values[b], values[b + 1] = values[b + 1], values[b]
        return values

    @staticmethod
    def selection_sort(values):
        """
        iterate through values selecting smallest and moving to front O(n**2)
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.selection_sort(values)
        [1, 2, 3, 4, 5]
        """
        for i in range(len(values) - 1):
            smallest_index = i
            for j in range(i + 1, len(values)):
                if values[j] < values[smallest_index]:
                    smallest_index = j
            if smallest_index != i:
                values[i], values[smallest_index] = values[smallest_index], values[i]
        return values

    @staticmethod
    def insertion_sort(values):
        """
        iterate through values and insert value in proper position O(n**2)
        good for sorting small sequences, n < 50
        or sequences that are already nearly sorted
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.insertion_sort(values)
        [1, 2, 3, 4, 5]
        """
        for i in range(1, len(values)):
            j = i
            while j > 0 and values[j] < values[j - 1]:
                values[j], values[j - 1] = values[j - 1], values[j]
                j -= 1
        return values

    @staticmethod
    def heap_sort(values):
        """
        sort values by creating a heap and then popping from it O(nlogn)
        good for small to medium sequences that can fit in memory
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.heap_sort(values)
        [1, 2, 3, 4, 5]
        """
        heapq.heapify(values)
        values[:] = [heapq.heappop(values) for x in range(len(values))]

    @staticmethod
    def merge_sort(values):
        """
        divide list in 2(left, right) until each list is only 1 item long, and thus sorted
        then merge left and right together into a sorted list O(nlogn)
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.merge_sort(values)
        [1, 2, 3, 4, 5]
        less preferred than heap and quick for arrays that can fit in main memory
        works best for input in multiple locations
        """
        if len(values) <= 1:
            return values
        mid = len(values) // 2
        left = Sort.merge_sort(values[:mid])
        right = Sort.merge_sort(values[mid:])
        l, r = 0, 0
        for i in range(len(values)):
            left_value = left[l] if l < len(left) else None
            right_value = right[r] if r < len(right) else None
            if (left_value and right_value
                and  left_value < right_value) or right_value is None:
                values[i] = left_value
                l += 1
            elif (left_value and right_value
                  and  left_value > right_value) or left_value is None:
                values[i] = right_value
                r += 1
        return values

    @staticmethod
    def quick_sort(values):
        """
        pick pivot, put all items greater than pivot in larger, less than in smaller
        keep splitting until smaller and larger only 1 element, then combine O(nlogn)
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.quick_sort(values)
        [1, 2, 3, 4, 5]
        faster than heap and merge sort most of the time, however, not stable
        """
        if len(values) > 1:
            pivot = random.randint(0, len(values) - 1)
            smaller = []
            larger = []
            for i, value in enumerate(values):
                if i != pivot:
                    if value < values[pivot]:
                        smaller.append(value)
                    else:
                        larger.append(value)
            Sort.quick_sort(smaller)
            Sort.quick_sort(larger)
            values[:] = smaller + [values[pivot]] + larger
        return values

    @staticmethod
    def bucket_sort(values, N=100):
        """
        create a bucket ranging from 0 to N - 1, place item in bucket of its value
        then iterate through buckets and add to value
        must know range of values N in advance O(n+N) ~ O(n)
        works when N is less that nlogn
        >>> values = [1, 4, 3, 2, 5]
        >>> Sort.bucket_sort(values, 6)
        [1, 2, 3, 4, 5]
        good for arrays with small integer keys, character strings, etc from a discrete range
        """
        if len(values) == 0:
            return values
        buckets = [[] for x in range(N)]
        for value in reversed(values):
            buckets[value].append(value)
        values = []
        for bucket in buckets:
            while bucket:
                values.append(bucket.pop())
        return values

    @staticmethod
    def radix_sort(values, N=100):
        """
        sort list of key, value pairs using bucket sort on value
        then bucket sort on first value O(n+N) ~ O(n)
        >>> values = [[3, 3], [1, 5], [2, 5], [1, 2], [2, 3], [1, 7], [3, 2], [2, 2]]
        >>> Sort.radix_sort(values, 8)
        [[1, 2], [1, 5], [1, 7], [2, 2], [2, 3], [2, 5], [3, 2], [3, 3]]
        good for tuples of keys from a discrete range
        """
        if len(values) == 0:
            return values
        buckets = [[] for x in range(N)]
        for value in reversed(values):
            buckets[value[1]].append(value)
        values = []
        for bucket in buckets:
            while bucket:
                values.append(bucket.pop())
        buckets = [[] for x in range(N)]
        for value in reversed(values):
            buckets[value[0]].append(value)
        values = []
        for bucket in buckets:
            while bucket:
                values.append(bucket.pop())
        return values
