import os

class State:
    def __init__(this, game, data = {}):
        this.data = data
        this.game = game
        this.name = this.__class__.__name__
        this.oldScreen = ''
        print("initialized state",this.name)
        this.setupDone = False

    def trySetup(this):
        if not this.setupDone:
            this.setup()
            this.setupDone = True

    def setup():
        pass

    def update(this):
        pass

    def onEvent(this, ch):
        pass

    def clear(this):
        os.system("cls")

    def render(this, screen = False):
        if not screen:
            screen = this.oldScreen
        if screen != this.oldScreen:
            this.clear()
            print(screen)
            this.oldScreen = screen

