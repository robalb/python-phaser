from state import State

class Game:
    def __init__(this, state):
        this.state = state()

    def update(this):
        ret = this.state.update()
        if ret:
            this.state = ret

    def keyHandle(this, ch):
        print(ch)
        ret = this.state.onEvent(ch)
        if ret:
            this.state = ret
