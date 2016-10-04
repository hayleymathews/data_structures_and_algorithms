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
