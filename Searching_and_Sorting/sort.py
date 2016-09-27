"""python implementation of basic sort algorithms
bubble sort, selection sort, insertion sort """

class Sort:
    """
    various sorts
    """
    @staticmethod
    def bubble_sort(values):
        """
        iterate through values and bubble largest value to end O(n**2)
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
        """
        for i in range(1, len(values)):
            j = i
            while j > 0 and values[j] < values[j - 1]:
                values[j], values[j - 1] = values[j - 1], values[j]
                j -= 1
        return values

    @staticmethod
    def merge_sort(values):
        """
        divide list in 2(left, right) until each list is only 1 item long, and thus sorted
        then merge left and right together into a sorted list O(nlogn)
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
        """
        if len(values) > 1:
            pivot = len(values) // 2
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
