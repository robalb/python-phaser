from state import State
import random

class PipesState(State):

    #in order to allow box drawing characters on windows cmd, the charset
    #is set to cp437 (see https://en.wikipedia.org/wiki/Code_page_437)
    #the charset is set via the cmd command 'chcp 437'
    characters = {
        'line':{
            'up': 179,
            'right': 196,
            'down': 179,
            'left': 196,
            'start': 219
            },
        'block':{
            'up': 219,
            'right': 219,
            'down': 219,
            'left': 219,
            'start': 219
            },
        'fatLine':{
            'up': 186,
            'right': 205,
            'down': 186,
            'left': 205,
            'start': 219
            }
        }
    angleCharacters = {
        'line':{
            'up': {
                'right': 218,
                'left': 191
                },
            'down': {
                'right': 192,
                'left': 217
                },
            'right': {
                'up': 217,
                'down': 191
                },
            'left': {
                'up': 192,
                'down': 218
                }
            },
        'block':{
            'up': {
                'right': 219,
                'left': 219
                },
            'down': {
                'right': 219,
                'left': 219
                },
            'right': {
                'up': 219,
                'down': 219
                },
            'left': {
                'up': 219,
                'down': 219
                }
            },
        'fatLine':{
            'up': {
                'right': 201,
                'left': 187
                },
            'down': {
                'right': 200,
                'left': 188
                },
            'right': {
                'up': 188,
                'down': 187
                },
            'left': {
                'up': 200,
                'down': 201
                }
            }
        }
    characterStyles = ('line', 'fatLine')#the block style has been removed because it looks bad

    directions = ( 'up', 'right', 'down', 'left' )
    oppositeDirections = [
            ('up', 'down'),
            ('left', 'right')
            ]

    #the 'pipe' data. this could be implemented into a class, in order to have
    #multiple moving pipes
    x = 0
    y = 2
    ch = ''
    charStyle = 'line'
    direction = 'down'

    def setup(this):
        this.game.cmd("chcp 437")
        this.game.tick = 100
        this.y = this.game.height // 2
        this.x = this.game.width // 2

    def printCartesian(this, x, y, ch):
        y = this.game.height - y - 1
        this.game.printAt(y, x, ch)

    def getAngleCharacter(this, oldDirection, newDirection):
        return this.angleCharacters[this.charStyle][oldDirection][newDirection]

    def getStraightCharacter(this, direction):
        return this.characters[this.charStyle][direction]

    def generateNewDirection(this, currentDirection):
        #generate new random direction
        newDirectionIndex = random.randint(0,len(this.directions)-1)
        newDirection = this.directions[newDirectionIndex]
        #check that the new direction is not the same
        #or the opposite of the current one
        isGood = True
        for oppositePair in this.oppositeDirections:
            if newDirection in oppositePair and currentDirection in oppositePair:
                isGood = False
                break

        if isGood:
            return newDirection
        return False


    def update(this):
        #move the pipe
        if this.direction == 'up':
            this.y+= 1
        elif this.direction == 'down':
            this.y -= 1
        elif this.direction == 'left':
            this.x -= 1
        elif this.direction == 'right':
            this.x += 1

        #change the direction every random tick, and update the pipe aspect accordingly
        this.ch = this.getStraightCharacter(this.direction)
        if random.randint(0,20) < 5:
            newDirection = this.generateNewDirection(this.direction)
            if newDirection:
                this.ch = this.getAngleCharacter(this.direction, newDirection)
                this.direction = newDirection

        #change the character style of the pipe
        if random.randint(0,1000) < 5:
            this.charStyle = this.characterStyles[random.randint(0,len(this.characterStyles)-1)]

        #warp the pipe position when it goes outside the borders. pacman style
        if this.x < 0:
            this.x = this.game.width - 1
        if this.x > this.game.width -1:
            this.x = 0

        if this.y < 0:
            this.y = this.game.height -1
        if this.y > this.game.height -1:
            this.y = 0

        #print the pipe
        this.printCartesian(this.x, this.y, chr(this.ch))


