"""python implementation of basic sort algorithms
bubble sort, selection sort, insertion sort """

class Sort:
    """
    various sorts
    """

    def bubble_sort(values):
        """
        iterate through values and bubble largest value to end O(n**2)
        """
        for a in range(len(values) - 1):
            for b  in range(len(values[:-a])):
                if values[b] > values[b + 1]:
                    values[b], values[b + 1] = values[b+1], values[b]
        return values

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

    def insertion_sort(values):
        """
        iterate through values and insert value in proper position O(n**2)
        """
        pass
