"""
python implementations of various text algorithms
"""
import functools

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
        if not text or not pattern:
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

    @staticmethod
    def find_patterns_trie(text, patterns):
        """
        find indices of patterns in text using trie data structure
        """
        pass

    @staticmethod
    def longest_common_subsequence(text, other):
        """
        find longest common subsequence of two strings O(nm)
        >>> text, other = 'GTTCCTAATA', 'CGATAATTGAGA'
        >>> Text.longest_common_subsequence(text, other)
        'GTTTAA'
        """
        n, m = len(text), len(other)
        longest = [[0] * (m + 1) for x in range(n + 1)]
        for x in range(n):
            for y in range(m):
                if text[x] == other[y]:
                    longest[x + 1][y + 1] = longest[x][y] + 1
                else:
                    longest[x + 1][y + 1] = max(longest[x][y + 1],
                                                longest[x + 1][y])
        solution = []
        while longest[n][m] > 0:
            if text[n - 1] == other[m - 1]:
                solution.append(text[n - 1])
                n -= 1
                m -= 1
            elif longest[n - 1][m] >= longest[n][m - 1]:
                n -= 1
            else:
                m -= 1
        return ''.join(reversed(solution))

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def memoized_lcs(text, other):
        """
        longest common subsequence using memoization and caching O(nm)
        more overhead for memoization, but does less work than dynamic programming
        >>> text, other = "GTACGGTTC", "CGATTGGAA"
        >>> Text.memoized_lcs(text, other)
        'CGTT'
        """
        if not text or not other:
            return ''
        if text[0] == other[0]:
            return text[0] + Text.memoized_lcs(text[1:], other[1:])
        else:
            return max(Text.memoized_lcs(text[1:], other),
                       Text.memoized_lcs(text, other[1:]), key=len)

    @staticmethod
    def huffman_encode(text):
        """
        encode text to bits where most frequent characters get shortest bit length
        for text length n and distinct characters d O(n + dlogd)
        """
        pass
