import msvcrt
import os
import time
from state import State

class Game:
    #the current state object
    state = False
    #a boolean that controls the game infinite loop
    _isRunning = False
    #data to handle key input
    _isArrow = False
    _arrows = {
        72: "up",
        80: "down",
        75: "left",
        77: "right"
        }
    #the current game tick speed
    tick = 0
    #attribute to control the tick speed
    _millis = False
    #a string containing the current data to draw on screen
    _screenBuffer = False

    def __init__(this, options = { 'width': 80, 'height': 25, 'tick': 25 }):
        this.width, this.height, this.tick = options.values()

    #method called to start or unpause the game
    #param: the first state class
    def start(this, state = False):
        if state:
            this.state = state()
        elif not this.state:
            return
        this._isRunning = True
        this._tick()

    def pause(this):
        this._isRunning = False

    def stop(this):
        this._isRunning = False
        this.state = False
        raise SystemExit


    def clear(this):
        os.system("cls")

    def render(this, screen = False):
        if not screen:
            screen = this._screenBuffer
        if screen != this._screenBuffer:
            this.clear()
            print(screen)
            this._screenBuffer = screen


    #method that executes on loop, and
    #calls the update and keyPress methods of the current state
    def _tick(this):
        while this._isRunning:
            this._update()
            if msvcrt.kbhit():
                c = msvcrt.getch()
                asc = ord(c)
                if this._isArrow:
                    this._isArrow = False
                    this._keyPress(this._arrows[asc])
                else:
                    if asc == 224:
                        this._isArrow = True
                    else:
                        this._keyPress(chr(asc))


    #method that controls the amount of times the update method of the current
    #state can be called
    def _update(this):
        millis = int(round(time.time() * 1000))
        if not this._millis or (millis - this._millis) > 1000 / this.tick:
            this._millis = millis
            ret = this.state.update()
            if ret:
                this.state = ret

    def _keyPress(this, ch):
        ret = this.state.onEvent(ch)
        if ret:
            this.state = ret
