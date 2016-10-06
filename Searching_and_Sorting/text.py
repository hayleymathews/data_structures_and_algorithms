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

    @staticmethod
    def find_pattern_knuth_morris_pratt(text, pattern):
        """
        knuth morris pratt algorithm to find first index of pattern in text O(n + m)
        >>> text, pattern = 'atcggctatt', 'tat'
        >>> Text.find_pattern_knuth_morris_pratt(text, pattern)
        6
        """
        n, m = len(text), len(pattern)
        if m == 0:
            return 0
        fail = [0] * m
        j = 1
        k = 0
        while j < m:
            if pattern[j] == pattern[k]:
                fail[j] = k + 1
                j += 1
                k += 1
            elif k > 0:
                k = fail[k - 1]
            else:
                j += 1
        j = 0
        k = 0
        while j < n:
            if text[j] == pattern[k]:
                if k == m - 1:
                    return j - m + 1
                j += 1
                k += 1
            elif k > 0:
                k = fail[k - 1]
            else:
                j += 1
        return -1
