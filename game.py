from state import State

class Game:
    def __init__(this, state):
        this.currentstate = state()
        this.state = State

    def update(this):
        this.state.update()

    def keyHandle(this, ch):
        print(ch)
        this.state = this.state.onEvent(ch)
        this.state.trySetup()
