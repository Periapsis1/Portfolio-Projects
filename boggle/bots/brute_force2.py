
import random

class Bot:
    name = 'brute_force2'
    description = "generates random chains until they're valid words, and prioritizes long words"
    def __init__(self, board, word_list):
        self.board = board
        self.h = len(board)
        self.w = len(board[0])
        self.word_list = word_list
        self.history = []

    def chain_to_word(self, coords):
        word = ''
        for i, j in coords:
            word += self.board[i][j]

        return word.lower()

    def validate_word(self, chain):
        word = self.chain_to_word(chain)
        return word in self.word_list

    def generate_word(self):
        length = self.w * self.h
        chain = [(random.randrange(0, self.h), random.randrange(0, self.w))]

        while len(chain) < length:
            i, j = chain[-1]
            neighbors = []
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if ii == i and jj == j:
                        continue

                    if (ii, jj) in chain:
                        continue

                    if 0 <= ii < self.h and 0 <= jj < self.w:
                        neighbors.append((ii, jj))
                    
            if len(neighbors) == 0:
                break

            chain.append(random.choice(neighbors))

            if self.validate_word(chain) and self.chain_to_word(chain) not in self.history:
                break

        return chain
                
    def submit_word(self, time_left):
        word = ()
        trials = 0
        max_trials = 10000
        while trials < max_trials and not self.word_list.get(self.chain_to_word(word), None):
            word = self.generate_word()
            
            trials += 1

        self.history.append(self.chain_to_word(word))
        return word
