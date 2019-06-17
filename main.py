
from states import *
from game import Game

options = {
        'width': 80,
        'height': 25,
        'tick': 100
        }
game = Game(options)
# print(game.width, game.height, game.tick) 
game.start(InitialState)


