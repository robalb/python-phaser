
#a template class that can help reduce the amount of boilerplate code
#in all game state classes by providing a setup function and setting the
#game and _receiveddata attributes
class State:
    def __init__(this, game, data = {}):
        this._receivedData = data
        this.game = game
        this.name = this.__class__.__name__
        this.setup()

    def setup(this):
        pass

    def update(this):
        pass

    def keyPress(this, ch):
        pass

