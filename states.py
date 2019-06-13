from state import State


class FinalState(State):

    def update(this):
        this.render(" game over ")


class MenuState(State):

    def setup(this):
        this.h = 0
        this.vel = 0
        this.gravity = 1200

    def update(this):
        this.vel = this.vel + 1
        if this.vel > this.gravity:
            this.vel = 0
            if this.h < 20:
                this.h = this.h + 1
            else:
                return FinalState()
        screen = "\n" * this.h
        screen = screen + "-" * 10
        this.render(screen)

    def onEvent(this, ch):
        print(ch)


class InitialState(State):

    def setup(this):
        pass

    def update(this):
        screen = "---------\n" * 10
        screen = screen + " premi spazio"
        screen = screen + "----------\n" * 10
        this.render()

    def onEvent(this, ch):
        print(ch)
        if ch == " ":
            return MenuState()




