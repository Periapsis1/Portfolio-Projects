'''
your own bot should have a class called Bot that has the following
    an optional name attribute
    an optional description attribute

    an __init__ method that takes in self, board, and word_list
    and a submit_word method which takes no arguments and return a list/tuple of coordinates corresponding to letters on the board that make up a word

any other class, function, method, or attribute is allowed

for coordinates, it follows row then column order, with indices starting from 0
so, for example, if I had the following board
    A B C D
    U R E F
    G H I J
    K L M N
then I would get
    (0, 1) = B
    (1, 1) = R
    (1, 0) = U
    (2, 1) = H
so the chain [(0, 1), (1, 1), (1, 0), (2, 1)] would correspond to "BRUH" and is a valid chain.
'''
class Bot:
    name = 'Example bot'
    description = 'An example of how the bot should be structured'
    def __init__(self, board, word_list):  # board and word_list can be named differently, but you must take these two args in, even if you don't store them
        # storing these is optional but highly recommended
        self.board = board
        self.word_list = word_list

    def submit_word(self, time_left):  # must accept 1 argument which will be time left, and return a list/tuple of coordinates
        return ((0, 0), (1, 1), (2, 2), (3, 3))