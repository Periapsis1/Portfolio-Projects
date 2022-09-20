
from os import sep
import random

def chain_to_word(board, chain):
    return ''.join(board[i][j] for i, j in chain).lower()

def get_neighbors(i, j=None):
    if j is None:
        i, j = i
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if ii == i and jj == j:
                continue

            if 0 <= ii < 4 and 0 <= jj < 4:
                yield (ii, jj)

def find_potential_chains(board, word, near=None, history=()):
    '''
    finds potential chains given the board and a word
    leave near and history blank unless you know what you're doing

    this doesn't return a list itself, it's a generator which means it
        yields values rather than returning them. You can either loop
        over this like
            for chain in find_potential_chains(board, word):
                ...
        or convert it to a list like
            chains = list(find_potential_chains(board, word))
        This is essentially so it can stop looking for chains if you've
        already found the desired chain.

    It yields nothing if it doesn't return anything. If you just want to check
    if a chain exists, just do any(find_potential_chains(board, word)). It returns
    true iff a chain is found, otherwise, if it couldn't find a valid chain, it returns False.
    Generators act weird if you try to use them more than once, so keep that in mind.
    My favorite way to use it is
        for chain in find_potential_chains(board, word):
            # do something with the chain
            break  # or return the chain depending on the context
        else:
            # didn't find a valid chain
    '''
    c = word[0]
    if near is not None:
        iter_ = get_neighbors(near)
    else:
        iter_ = ((i, j) for i in range(4) for j in range(4))
    for i, j in iter_:
        if (i, j) in history:
            continue
        if board[i][j] == c:
            pos = (i, j)
            if len(word) == 1:
                yield (pos,)
            else:
                for potential_chain in find_potential_chains(board, word[1:], near=pos, history=history + (pos,)):
                    yield (pos,) + potential_chain

def combine_chains(chain1, chain2):
    '''
    Combines two chains and returns the result if they can form a valid chain, otherwise returns None
    '''
    a = chain1[-1]
    b = chain2[0]
    if b in list(get_neighbors(*a)) and all(x not in chain2 for x in chain1):
        return chain1 + chain2

    else:
        return None

def test_chain_to_word():
    board = [
        'abcd',
        'efgh',
        'ijkl',
        'mnop'
    ]
    chain = ((2, 2), (3, 1), (2, 0), (1, 1), (1, 0))
    print('expected: knife, actual:', chain_to_word(board, chain))

def test_get_neighbors():
    print((0, 0), get_neighbors(0, 0))
    print((0, 1), get_neighbors(0, 1))
    print((1, 1), get_neighbors(1, 1))

def test_find_potential_chains():
    board = [
        'ytal',
        'whit',
        'nbcm',
        'veae'
    ]
    print(*find_potential_chains(board, 'milt'), sep='\n')
    print(any(find_potential_chains(board, 'amita')))
    print(*map(str,find_potential_chains(board, 'caeb')))

def main():
    test_chain_to_word()
    test_get_neighbors()
    test_find_potential_chains()

if __name__ == '__main__':
    main()