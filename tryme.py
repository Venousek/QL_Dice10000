import numpy as np
import math
from dice_game import DiceGame
from dice_combos import *
from qlplayer import QLPlayer, CircusSelector
from simpleplayer import DiceThresholdPlayer, HumanPlayer
import os

np.random.seed()
filename = 'trained_player.pkl'
simple_player = DiceThresholdPlayer(1)

allow_stealing = False
goal_score = 10_000
training_rounds = 10

checkers = [has3Pairs, hasStraight, HasM_Ns(1, 1), HasM_Ns(2, 1), HasM_Ns(1, 5), HasM_Ns(2, 5)]
for i in range(1,7):
    checkers.append(Has3(i))
    checkers.append(Has4(i))
    checkers.append(Has5(i))
    checkers.append(Has6(i))

if os.path.isfile(filename):
    trained_player = QLPlayer.from_file(filename)
    trained_player.state_converter = lambda x: (int(x[0]/100), x[1], x[2])
else:
    print('Generating and training a QL Player...')
    params = {}
    params['df'] = 0.9
    params['state_converter'] = lambda x: (int(x[0]/100), x[1], x[2])
    params['learn_select'] = CircusSelector(bias=200)
    trained_player = QLPlayer(params=params)

    for a in range(training_rounds):
        for i in range(1000):
            DiceGame([trained_player, simple_player], goal_score, verbose=False, stealing_mode=allow_stealing, checkers=checkers).play()
        print( '{} rounds of training complete...'.format((a+1)*1000) )
        trained_player.lr /= 1.414
        trained_player.learn_select.bias /= 1.414

    trained_player.is_learning = False
    trained_player.to_file(filename)

p1 = HumanPlayer()
p2 = trained_player

players = [p1, p2]

p1tag = input('Type in your name (then enter): ')
p2tag = 'QL Player'

scores = DiceGame(players, goal_score, tags=[p1tag, p2tag], verbose=True, stealing_mode=allow_stealing, checkers=checkers).play()