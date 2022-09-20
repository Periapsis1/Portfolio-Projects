import game
import os
import itertools
import importlib
import numpy as np
import random
import math
import json

STRATEGY_FOLDER = "bots"
RESULTS_FILE = "results.txt"

os.chdir(os.path.dirname(__file__))

def do_one_game(g=None, time_per_player=1, turns_per_player=100, w=4, h=4):
    bots = []
    for file in os.listdir(STRATEGY_FOLDER):
        if file.endswith('.py'):
            module = file[:-3]
            bot_module = importlib.import_module(STRATEGY_FOLDER+'.'+module)
            if 'Bot' in bot_module.__dict__:
                if 'name' not in bot_module.Bot.__dict__:
                    bot_module.Bot.name = module
                if 'description' not in bot_module.Bot.__dict__:
                    bot_module.Bot.description = ''
                bots.append(bot_module.Bot)

    if g is None:
        g = game.Game(bots, w=w, h=h)

    results = g.run_game(time_per_player=time_per_player, turns_per_player=turns_per_player)

    g.print_results(results)


def do_n_games(n, time_per_player=1, turns_per_player=100, w=4, h=4):
    for _ in range(n):
        do_one_game(time_per_player=time_per_player, turns_per_player=turns_per_player, w=w, h=h)

def main():
    do_n_games(1, time_per_player=0.1, turns_per_player=100000, w=16, h=16)

if __name__ == '__main__':
    main()
    