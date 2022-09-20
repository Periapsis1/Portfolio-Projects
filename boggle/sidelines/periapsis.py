'''
Graph
3 5 5 3
5 8 8 5
5 8 8 5
3 5 5 3

average neighbors = 5.25

upper-bound = 5.25^16

number of total paths = 343,184
^ Hamiltonian paths*
'''


import re
#import helper_funcs
import random
import time

plural_exceptions = {
    'mouse':'mice',
    'moose':'moose',
    'goose':'geese',
    'person':'people',
    'child':'children',
}

def pluralize(word:str):
    word = word.lower()
    if word in plural_exceptions:
        return plural_exceptions[word]
    elif re.match(r'^.*man$', word):
        return word[:-3] + 'men'
    elif re.match(r'^.*[^aeiou]y$', word):
        return word[:-1] + 'ies'
    elif re.match(r'^.*us$', word):
        return word[:-2] + 'ii'
    elif re.match(r'^.*(s|ch|sh)$', word):
        return word + 'es'
    elif re.match(r'^.*(f|fe)$', word):
        return (word[:-2] if word[-2:] == 'fe' else word[:-1]) + 'ves'
    else:
        return word + 's'

class Bot:
    name = 'Periapsis'
    description = ""
    def __init__(self, board, word_list):
        self.i = 0
        self.h = len(board)
        self.w = len(board[0])
        self.board = board
        self.word_list = word_list
        self.queue = []  # priority queue based on length
        self.history = []
        self.prefix_chains = []
        self.filtered_words = []
        self.find_prefixes()

        #self.filter_words()
        #self.populate_words(10)

    def filter_words(self):
        letters = ''.join(''.join(row) for row in self.board).lower()
        for word in self.word_list.keys():
            if all(l in letters for l in word):
                self.filtered_words.append(word)

        print(len(self.filtered_words))

    def get_neighbors(self, i, j):
        for ii, jj in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
            if 0 <= ii < self.h and 0 <= jj < self.w:
                yield (ii, jj)

    def find_potential_chains(self, word, near=None, history=()):
        c = word[0]
        if c == 'q':
            c = 'qu'
            word = word[2:]
        else:
            word = word[1:]
        if near is not None and c in self.ltc:
            for i, j in self.get_neighbors(*near):
                if (i, j) in history:
                    continue
                pos = (i, j)
                if len(word) == 0:
                    yield (pos,)
                    break
                else:
                    for chain in self.find_potential_chains(word, near=pos, history=history + (pos,)):
                        yield (pos,) + chain
        else:
            for i, j in self.ltc[c]:
                pos = (i, j)
                if len(word) == 0:
                    yield (pos,)
                    break
                for chain in self.find_potential_chains(word, near=pos, history=history + (pos,)):
                    yield (pos,) + chain

    def find_prefixes(self):
        for prefix in (
            'un',
            're',
            'bi',
            'in',
            'sub',
        ):
            for chain in self.find_potential_chains(prefix):
                self.prefix_chains.append(chain)
                    

    def chain_to_word(self, coords):
        word = ''
        for i, j in coords:
            word += self.board[i][j]

        return word.lower()

    def combine_chains(self, c1, c2):
        a = c1[-1]
        b = c2[-1]
        if b in [*self.get_neighbors(*a)] and all(x not in c2 for x in c1):
            return c1 + c2
        else:
            return None
    def try_reverse(self, chain):
        self.add_chain_if_valid(chain[::-1])

    def try_plural(self, coords):
        plural = pluralize(self.chain_to_word(coords))
        self.add_word_if_valid(plural)

    def try_prefix(self, chain):
        for prefix in self.prefix_chains:
            self.add_chain_if_valid(self.combine_chains(prefix, chain))

    def add_word_if_valid(self, word):
        if word in self.history:
            return False
        
        if word in self.word_list:
            for chain in self.find_potential_chains(word):
                self.add_chain_if_valid(chain)
                return True
        
        return False

    def add_chain_if_valid(self, chain):
        if type(chain) not in (list, tuple):
            return False
        
        word = self.chain_to_word(chain)
        
        if word in self.history or not self.validate_word(chain):
            return False

        self.queue.append(chain)
        self.history.append(word)
        return True

    def validate_word(self, chain):
        word = self.chain_to_word(chain)
        return word in self.word_list

    def generate_words(self):
        length = 16
        chain = [(random.randrange(0, 4), random.randrange(0, 4))]

        while len(chain) < length:
            i, j = chain[-1]
            neighbors = [n for n in self.get_neighbors(i, j) if n not in chain]
                    
            if len(neighbors) == 0:
                break

            chain.append(random.choice(neighbors))
            word = self.chain_to_word(chain)

            if len(chain) > 2 and word not in self.history and self.validate_word(chain):
                tchain = tuple(chain)
                self.queue.append(tchain)
                self.try_reverse(tchain)
                #self.try_plural(tchain)
                #self.try_prefix(tchain)
                self.history.append(word)

    def populate_words(self, t):
        a = time.perf_counter()
        while time.perf_counter() - a < t:
            self.generate_words()
                
    def submit_word(self, time_left):
        if time_left > 0.01:
            self.populate_words(time_left - 0.01)

        self.queue.sort(key=lambda c:len(self.chain_to_word(c)), reverse=True)

        if self.i < len(self.queue):
            choice = self.queue.pop(0)
            return choice
        else:
            return ()