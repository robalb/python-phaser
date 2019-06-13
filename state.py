import os

class State:
    def __init__(this, data = {}):
        this.data = data
        # this.game = game
        this.name = this.__class__.__name__
        this.oldScreen = ''
        this.tick = 0
        this.tickSpeed = 1
        print("initialized state",this.name)
        this.setup()

    def setup(this):
        pass

    def _update(this):
        this.tick += 1
        if this.tick > this.tickSpeed:
            this.tick = 0
            return this.update()

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

