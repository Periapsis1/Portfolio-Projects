
#import helper_funcs
import random
import time
import timeit

class Bot:
    name = 'Periapsis 2'
    desc = '''
    Filters all words based on if all letters exist on the board.
    Then goes through them and turns them into chains if possible (letters touching. doesn't use same square)
    Then sorts from longest to shortest in a queue
    Then submits them in order
    '''
    def __init__(self, board, word_list):
        self.board = board
        self.h = len(board)
        self.w = len(board[0])
        self.word_list = word_list
        self.queue = []
        self.filtered_words = []
        self.beginning = True
        self.ctl = {}  # coord to letter
        self.ltc = {}  # letter to coords
        self.neighbors = {} # neighbors for each node
        self.priority = {} # priority for length of words
        self.k = 0
                
        #print('time to setup:', timeit.timeit(self.filter_words, number=1))
        #self.filter_words()

    def setup(self, t):  # set up some lookup tables
        for i in range(self.h):
            for j in range(self.w):  # for every coordinate on the board
                c = self.board[i][j]
                if c not in self.ltc:
                    self.ltc[c] = set()
                self.ltc[c].add((i, j))  # map letters to coords
                self.ctl[(i, j)] = c  # map coords to their letter
                self.neighbors[(i, j)] = set(self.get_neighbors(i, j))  # map neighbors to coords
        
        if t > 1:
            priority = -1  # not much of a time crunch, find all words
        else:
            priority = 100  # time crunch, find 100 words from each category
        
        for l in range(3, self.h * self.w + 1):
            self.priority[l] = priority

    def find_potential_chains(self, word, near=None, history=()):
        ''' cat
        a b c d
        x a t m
        b r u h
        c c c c
        '''
        c = word[0]
        if c == 'q':
            c = 'qu'
            word = word[2:]
        else:
            word = word[1:]
        if near is not None:  # recursive step
            for i, j in self.neighbors[near] & self.ltc[c]:  # intersection of ltc and neighbors of near
                if (i, j) in history:
                    continue
                pos = (i, j)
                if len(word) == 0:
                    yield (pos,)
                    break
                else:
                    for chain in self.find_potential_chains(word, near=pos, history=history + (pos,)):
                        yield (pos,) + chain
        else:  # first step
            for i, j in self.ltc[c]:
                pos = (i, j)
                if len(word) == 0:
                    yield (pos,)
                    break
                for chain in self.find_potential_chains(word, near=pos, history=history + (pos,)):
                    yield (pos,) + chain
    
    def filter_words(self, t=None):
        a = time.time()
        letters = set(''.join(''.join(row) for row in self.board))
        wh = self.w * self.h  # longest possible word
        for word in sorted(self.word_list.keys(), key=len):  # all words sorted from shortest to longest
            if self.priority.get(len(word), 0) != 0 and all(l in letters for l in word):  # if we're looking for words of this length, and all letters in the word are on the baord...
                for chain in self.find_potential_chains(word):
                    self.queue.append(chain)  # take the first chain found and add it to the queue
                    self.priority[len(word)] -= 1  # update the priority
                    break
            if t is not None and time.time() - a >= t:
                break  # break if we're about to run out of time

        self.queue.sort(key=len)  # sort the queue. technically unnecessary since the word list is sorted, but it's fast anyway so it doesn't matter lol

    def get_neighbors(self, i, j):
        for ii, jj in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
            if 0 <= ii < self.h and 0 <= jj < self.w:
                yield (ii, jj)

    def submit_word(self, t):
        if self.beginning:
            if t <= 10:
                tt = t - 0.01
            else:
                tt = t * 0.999
            self.setup(t)
            self.filter_words(tt)
            self.beginning = False
        if self.queue:
            return self.queue.pop()
        else:
            return None

if __name__ == "__main__":
    import dis

    dis.dis(Bot)