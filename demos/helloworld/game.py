import msvcrt
from ctypes import *
import os
import time
import winsound
from cursorHide import hideCursor, showCursor
from cursorMove import printAt

#
# this is a state-based, lightweight game library
# for python cli applications on windows.
# this library has been tested and works on windows 10,8,7 and xp
# game methods:
# - start(stateClass, data)
# - pause()
# - stop()
# - note(frequency, duration)
# - clear()
# - render(string)
# - printAt(x, y, string)
#
# the stateClass passed as parameter for the game.start method should have
# the following methods:
# - __init__(this, gameObject, optionalData)
# - update()
# - keyPress(ch)
#
class Game:
    #the current state object
    state = False
    #a boolean that controls the game infinite loop
    _isRunning = False
    #boolean variable used to handle arrow inputs (see the keyPress method)
    _isArrow = False
    #keywords that facilitate input handling in game states
    _arrows = {
        72: "up",
        80: "down",
        75: "left",
        77: "right"
        }
    _keys = {
        13: 'enter',
        27: 'esc'
        }
    #the current game tick speed
    tick = 0
    #attribute to control the tick speed
    _millis = False
    #a string containing the current data to draw on screen
    _screenBuffer = False

    def __init__(this, options = { 'width': 80, 'height': 25, 'tick': 25, 'title': False }):
        this.width, this.height, this.tick, title = options.values()
        #set the window title
        if title: os.system("title " + title)
        #set the window size to the current game size
        os.system("mode con: cols="+str(this.width)+" lines="+str(this.height))
        #hide the cursor to improve animations
        hideCursor()

    #method called to start a state or unpause the game
    #param: the first state class
    def start(this, state = False, data = {}):
        if state:
            this.state = state(this, data)
        elif not this.state:
            return
        this._isRunning = True
        this._tick()

    #pause the game. in order to unpause it, a call to the start method
    #is necessary. Use no parameters to recover from the exact moment the game was paused, or
    #use a state class reference as parameter to start a new state
    def pause(this):
        this._isRunning = False

    #stop the game and close the python program
    def stop(this):
        this._isRunning = False
        this.state = False
        showCursor()
        raise SystemExit

    #plays a note with the given frequency and time.
    #note: the note function will completely pause the game until it stops playing,
    #so in order to avoid lag, notes and the gametick should be scheduled accordingly
    def note(this, note, t):
        if t < this._millis:
            this._millis -= t
        else:
            this._millis = 1
        winsound.Beep(note, t)

    #set the game color using the windows command 'color'
    def setColor(this, color):
        os.system("color "+color)

    #execute cmd command
    def cmd(this, cmd):
        os.system(cmd)
        this.clear()

    #clear the screen
    def clear(this):
        os.system("cls")

    #clear the screen and print the string passed as parameter.
    #this function is optimized for printing several times per second.
    def render(this, screen = False):
        if not screen:
            screen = this._screenBuffer
        if screen != this._screenBuffer:
            this.clear()
            print(screen)
            this._screenBuffer = screen

    def printAt(this, x, y, text):
        printAt(x, y, text)



    #internal method that executes on loop, and
    #calls the update and keyPress methods of the current state
    def _tick(this):
        while this._isRunning:
            this._update()
            if msvcrt.kbhit():
                c = msvcrt.getch()
                this._keyPress(c)


    #internal method that controls the amount of times the update method of the current
    #state can be called, and calls it
    def _update(this):
        millis = int(round(time.time() * 1000))
        if not this._millis or (millis - this._millis) > 1000 / this.tick:
            this._millis = millis
            this.state.update()

    #internal method that calls the keypress method of the current state, passing the
    #input letter as a char or, in case of a non ascii input such as left,right or esc, as a 
    #string describing the input
    def _keyPress(this, ch):
        asc = ord(ch)
        if this._isArrow:
            this._isArrow = False
            this.state.keyPress(this._arrows[asc])
        else:
            if asc == 224:
                this._isArrow = True
            elif asc in this._keys.keys():
                this.state.keyPress(this._keys[asc])
            else:
                this.state.keyPress(chr(asc))

