import msvcrt

from states import *
from game import Game


game = Game(InitialState)

arrow = False
arrows = {
    72: "up",
    80: "down",
    75: "left",
    77: "right"
    }

#main input listener loop
while True:
    game.update()
    if msvcrt.kbhit():
        c = msvcrt.getch()
        asc = ord(c)
        if arrow:
            arrow = False
            game.keyHandle(arrows[asc])
        else:
            if asc == 224:
                arrow = True
            else:
                game.keyHandle(chr(asc))




