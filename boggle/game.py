import math
import random
import time
import copy
import threading

import load_words

class Game:
    def __init__(self, players, board=None, w=4, h=4):
        self.w = w
        self.h = h
        if board is None:
            board = create_board(w, h)
        self.players = []
        for player in players:
            try:
                self.players.append(player(copy.deepcopy(board), wordList))
            except Exception as e:
                print(f'{player.name} constructor method failed: {e}')
        self.board = board
        self.neighbors = self.create_neighbor_map()

    def create_neighbor_map(self):
        coord_neighbors = {}
        w, h = self.w, self.h
        for i in range(h):
            for j in range(w):
                neighbors = ()
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if ii == i and jj == j:  # same square
                            continue
                        elif 0 <= ii < h or 0 <= jj < w:  # on the board
                            neighbors += ((ii, jj),)

                coord_neighbors[(i, j)] = neighbors
        return coord_neighbors

    def run_game(self, time_per_player=1, turns_per_player=100):
        words = {p.name:(p, []) for p in self.players}
        for player, players_words in words.values():  # get player object and their words
            time_left = time_per_player
            turns_left = turns_per_player
            while time_left > 0 and turns_left > 0:
                a = time.perf_counter()
                chain = player.submit_word(time_left)
                b = time.perf_counter()
                time_taken = b - a
                time_left -= time_taken
                turns_left -= 1
                if chain is None:
                    break
                if self.validate_chain(chain):
                    word = self.chain_to_word(chain)
                    if word not in players_words and self.validate_word(word):  # not a duplicate and word exists
                        players_words.append(word)

        scores = self.evaluate_words(words)
        results = {}
        for name, score in scores.items():
            word_list = words[name][1]
            results[name] = score, word_list
        return results

    def print_results(self, results):
        print('Board:')
        print('\n'.join(' '.join(row) for row in self.board))
        print()
        for name, (score, words) in results.items():
            print(f'{name}: {score}')
            #print(f'Wwords:')
            #print(' '.join((f"--{word}--" if not self.validate_word(word) else word) for word in words))
            #print('---------------------------')

    def validate_word(self, word):
        return wordList.get(word, None)

    def validate_chain(self, chain):
        history = []
        if type(chain) not in (list, tuple):  # not even a list/tuple
            return False

        chain = tuple(chain)
        
        if len(chain) < 3 or len(chain) > (self.w * self.h):  # too short or too long
            return False
        
        for pos in chain:
            if pos not in self.neighbors.keys():  # pos isn't on board or looks weird
                return False
        
        for pos1, pos2 in zip(chain, chain[1:]):
            history.append(pos1)
            if pos2 in history:  # position already used
                return False
            elif pos2 not in self.neighbors[pos1]:  # pos2 not connected to pos1
                return False
            
        word = self.chain_to_word(chain)  # combine letters
        
        return wordList.get(word.lower(), None)  # returns 1 if word exists, None otherwise

    def chain_to_word(self, chain):
        return ''.join(self.board[i][j] for i, j in chain).lower()

    def evaluate_words(self, words):
        scores = {}
        for i, (p1name, (p1, word_list1)) in enumerate(words.items()):  # loop over players
            ''' uncomment to delete copies when scoring and only allow unique words
            copied_words = []
            # first, remove duplicates
            for word in word_list1:
                for p2name, (p2, word_list2) in tuple(words.items())[i + 1:]:  # previous players already looped over this one and removed duplicates, so loop over next players
                    if word in word_list2:
                        copied_words.append(word)
                        word_list2.remove(word)
            
            for word in set(copied_words):
                word_list1.remove(word)
            '''
            # next, score player
            score = 0
            num_fails = 0
            for word in word_list1:
                if self.validate_word(word):
                    score += score_word(word)  # score based on length
                else:  # remove points for being badmegalul (this never actually runs)
                    num_fails += 1
                    score -= num_fails
            
            scores[p1name] = score
        return scores

def score_word(word):
    l = len(word)
    if l == 3 or l == 4:
        return 1
    elif l == 5:
        return 2
    elif l == 6:
        return 3
    elif l == 7:
        return 5
    elif l >= 8:
        return 11

def roll_dice(num=16):
    dice = copy.deepcopy(diceList)
    random.shuffle(dice)
    if num > 16:
        dice += random.choices(dice, k=num - 16)
    elif num < 16:
        dice = dice[:num]
    
    letters = []
    for d in dice:
        letters.append(random.choice(d).lower())

    return letters

def create_board(w=4,h=4):
    random.seed(696969)
    letters = roll_dice(w*h)
    return [[letters[i*h + j] for j in range(w)] for i in range(h)]



wordList = load_words.load()

diceList = [
    ["R","I","F","O","B","X"],
    ["I","F","E","H","E","Y"],
    ["D","E","N","O","W","S"],
    ["U","T","O","K","N","D"],
    ["H","M","S","R","A","O"],
    ["L","U","P","E","T","S"],
    ["A","C","I","T","O","A"],
    ["Y","L","G","K","U","E"],
    ["Qu","B","M","J","O","A"],
    ["E","H","I","S","P","N"],
    ["V","E","T","I","G","N"],
    ["B","A","L","I","Y","T"],
    ["E","Z","A","V","N","D"],
    ["R","A","L","E","S","C"],
    ["U","W","I","L","R","G"],
    ["P","A","C","E","M","D"]
]

def test():
    print()

if __name__ == "__main__":
    print('\n'.join(' '.join(row) for row in create_board()))