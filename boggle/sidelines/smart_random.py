
import random

class Bot:
    name = 'smart_random'
    description = "Returns random chains but they're actually chains"
    def __init__(self, board, word_list):
        self.board = board
        self.h = len(board)
        self.w = len(board[0])
        self.word_list = word_list

    def submit_word(self, time_left):
        length = random.randint(3, self.h * self.w)
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

                    if 0 <= ii < 4 and 0 <= jj < 4:
                        neighbors.append((ii, jj))
                    
            if len(neighbors) == 0:
                break

            chain.append(random.choice(neighbors))

        return chain
                