#import helper_funcs
import random
import time

class Bot:
    name = 'brute_force3'
    description = "finds as many words as it can in the first 90% of the match, then returns the longest ones"
    def __init__(self, board, word_list):
        self.i = 0
        self.board = board
        self.h = len(board)
        self.w = len(board[0])
        self.word_list = word_list
        self.queue = []  # priority queue based on length
        self.history = []

    def chain_to_word(self, coords):
        word = ''
        for i, j in coords:
            word += self.board[i][j]

        return word.lower()

    def get_neighbors(self, i, j):
        for ii in range(i - 1, i + 2):
            for jj in range(j - 1, j + 2):
                if ii == i and jj == j:
                    continue

                if 0 <= ii < self.h and 0 <= jj < self.w:
                    yield (ii, jj)

    def validate_word(self, chain):
        word = self.chain_to_word(chain)
        return self.word_list.get(word, None)  # 

    def generate_words(self):
        length = 16
        chain = [(random.randrange(0, self.h), random.randrange(0, self.w))]

        while len(chain) < length:
            i, j = chain[-1]
            neighbors = [n for n in self.get_neighbors(i, j) if n not in chain]
                    
            if len(neighbors) == 0:
                break

            chain.append(random.choice(neighbors))
            word = self.chain_to_word(chain)

            if len(chain) > 2 and word not in self.history and self.validate_word(chain):
                self.queue.append(tuple(chain))
                self.history.append(word)

    def populate_words(self, t):
        a = time.perf_counter()
        while time.perf_counter() - a < t - 0.1:
            self.generate_words()
                
    def submit_word(self, time_left):
        if time_left > 0.1:
            self.populate_words(time_left)

            self.queue.sort(key=lambda c:len(self.chain_to_word(c)), reverse=True)

        if self.i < len(self.queue):
            choice = self.queue[self.i]
            self.i += 1
            return choice
        else:
            return ()