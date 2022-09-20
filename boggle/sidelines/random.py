
import random

class Bot:
    name = 'Random'
    description = 'submits completely random coordinates'
    def __init__(self, board, word_list):
        self.board = board
        self.h = len(board)
        self.w = len(board[0])
        self.word_list = word_list

    def submit_word(self, time_left):
        length = random.randint(3, self.w * self.h)
        chain = []
        for _ in range(length):
            chain.append((random.randrange(0, self.h), random.randrange(0, self.w)))

        return chain