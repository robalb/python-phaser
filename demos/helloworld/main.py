
from states import *
from game import Game



#note: widths greater that 80 are only allowed in windows 10
options = {
        'width': 80,
        'height': 25,
        'tick': 100,
        'title': 'hello world demo'
        }
#initialize the game object
game = Game(options)
#start the InitialState game state
game.start(InitialState)
