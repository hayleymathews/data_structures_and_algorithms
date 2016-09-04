"""example using Array* to make game scoreboard
* really just Python List which is a Dynamic Array
>>> s = Scoreboard(2)
>>> s.add(GameEntry('French Stewart', -17000))
>>> s.add(GameEntry('Sean Connery', -230000))
>>> s.add(GameEntry('Burt Reynolds', 14))
>>> s
(Burt Reynolds, 14)
(French Stewart, -17000)
"""

class GameEntry:
    """
    represents an entry in a list of high scores
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '({0}, {1})'.format(self.name, self.score)

    def get_name(self):
        """
        gets name for entry
        """
        return self.name

    def get_score(self):
        """
        gets score for entry
        """
        return self.score

class Scoreboard:
    """
    fixed length sequence of high scores in ascending order
    """
    def __init__(self, capacity=10):
        self.board = [None] * capacity
        self.size = 0

    def __getitem__(self, index):
        return self.board[index]

    def __repr__(self):
        return '\n'.join(str(self.board[x]) for x in range(self.size))

    def add(self, entry):
        """
        add entry to high scores list if higher than an item in it O(n)
        """
        score = entry.get_score()
        if self.size < len(self.board) or score > self.board[-1].get_score():
            if self.size < len(self.board):
                self.size += 1
            index = self.size - 1
            while index > 0 and self.board[index - 1].get_score() < score:
                self.board[index] = self.board[index - 1]
                index -= 1
            self.board[index] = entry
