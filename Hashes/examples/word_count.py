"""count words in a file using map - reduce"""

def word_count(filename):
    freq = {}
    for piece in open(filename).read().lower().split():
        word = ' '.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word, 0)

    max_word = ''
    max_count = 0
    for (word, count) in freq.items():
        if count > max_count:
            max_count =  count
            max_word = word

    return max_word, max_count        
