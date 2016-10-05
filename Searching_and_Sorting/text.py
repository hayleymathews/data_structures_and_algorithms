"""
python implementations of various text algorithms
"""

class Text:
    """
    text algos
    """

    @staticmethod
    def find_pattern_brute(text, pattern):
        """
        brute force find first index of pattern in text if exists O(nm)
        >>> text, pattern = 'atcggctatt', 'tat'
        >>> Text.find_pattern_brute(text, pattern)
        6
        """
        n, m = len(text), len(pattern)
        for index in range(n - m + 1):
            k = 0
            while k < m and text[index + k] == pattern[k]:
                k += 1
            if k == m:
                return index
        return -1

    @staticmethod
    def find_pattern_boyer_moore(text, pattern):
        """
        boyer moore algorithm to find first index of pattern in text O(nm)
        >>> text, pattern = 'atcggctatt', 'tat'
        >>> Text.find_pattern_boyer_moore(text, pattern)
        6
        """
        n, m = len(text), len(pattern)
        if m == 0:
            return 0
        last = {pattern[x]: x for x in range(m)}
        i = m - 1
        k = m - 1
        while i < n:
            if text[i] == pattern[k]:
                if k == 0:
                    return i
                else:
                    i -= 1
                    k -= 1
            else:
                j = last.get(text[i], -1)
                i += m - min(k, j + 1)
                k = m - 1
        return -1
