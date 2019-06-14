from state import State
import os

class FinalState(State):
    asciiart="""

                     _______  _______  __   __  _______  
                    |       ||   _   ||  |_|  ||       | 
                    |    ___||  |_|  ||       ||    ___| 
                    |   | __ |       ||       ||   |___  
                    |   ||  ||       ||       ||    ___| 
                    |   |_| ||   _   || ||_|| ||   |___  
                    |_______||__| |__||_|   |_||_______| 
                     _______  __   __  _______  ______   
                    |       ||  | |  ||       ||    _ |  
                    |   _   ||  |_|  ||    ___||   | ||  
                    |  | |  ||       ||   |___ |   |_||_ 
                    |  |_|  ||       ||    ___||    __  |
                    |       | |     | |   |___ |   |  | |
                    |_______|  |___|  |_______||___|  |_|                                            
"""
    def setup(this):
        this.winner = this._receivedData['winner']

    def update(this):
        this.render(this.asciiart+ "\n"+str(this.winner))

class ScoreState(State):

    i = 0
    def setup(this):
        this.playerScores = this._receivedData['scores']
        this.tick = 1

    def update(this):
        score1 = this.playerScores[0]
        score2 = this.playerScores[1]
        if this.i == 2:
            return MultiplayerGameState(this._receivedData)
        if score1 == 5:
            return FinalState({'winner':1})
        elif score2 == 5:
            return FinalState({'winner':2})
        this.i += 1
        screen = "\n" * 10
        screen += " "*40
        screen += str(score1) + "-" + str(score2)
        this.render(screen)


class MultiplayerGameState(State):
    velx=1
    vely=1
    p1=0
    p2=0
    x=39
    y=10
    down=True
    right=True
    width = 80
    #bisogna lasciare una riga vuota
    #altrimenti la console va a capo e si perde la prima riga
    height = 23
    paddleHeight = 5
    counter=0
    def genstr(this,p1,p2,x,y):
        width = this.width
        height = this.height
        a=[]
        b=[' ' for i in range(width)]
        b.append('\n')
        st=''
        for i in range (height):
            a.append(b[:])
        for i in range (this.paddleHeight):
            a[p1+i][0]='|'
            a[p2+i][width-1]='|'
        a[y][x]='o'
        for i in range(height):
            for k in range(width):
                st+=a[i][k]
        return(st)

    def logic(this):
        if this.x==this.width-2:
            this.right=False
            if this.y>this.p2+4 or this.y<this.p2:
                return(1)
            else:
                this.tick+=1
        elif this.x==1:
            this.right=True
            if this.y>this.p1+4 or this.y<this.p1:
                return(2)
            else:
                this.tick+=1
        if this.right==True:
            this.x+=this.velx
        else:
            this.x-=this.velx
        if this.y==this.height-1:
            this.down=False
        elif this.y==0:
            this.down=True
        if this.down==True:
            this.y+=this.vely
        else:
            this.y-=this.vely
        return False
    #questa funzione viene chiamata solo una volta, al momento
    #della inizializzazione dello stato
    def setup(this):
        #imposta la velocita di gioco a 20 tick al secondo
        this.playerScores = this._receivedData['scores']
        this.tick = 10
        this.velx=1
        this.vely=1
        this.p1=0
        this.p2=0
        this.x=39
        this.y=10

    #questa funzione viene chiamata un botto di volte al secondo
    def update(this):
        winner = this.logic()
        if winner:
            this.playerScores[winner-1] += 1
            return ScoreState({'scores':this.playerScores})
        screen=this.genstr(this.p1,this.p2,this.x,this.y)
        this.render(screen)

    #questa funzione viene chiamata quando un tasto viene schiacciato
    def onEvent(this, ch):
        #player 1
        if ch == 'w':
            if this.p1 > 0: this.p1 -= 1
        elif ch == 's':
            if this.p1 < this.height-this.paddleHeight: this.p1 += 1
        #player 2
        if ch == 'up':
            if this.p2 > 0: this.p2 -= 1
        elif ch == 'down':
            if this.p2 < this.height-this.paddleHeight: this.p2 += 1
        #TODO: quit key




class InitialState(State):

    asciiArt3 = """
             _______  __   __  _______  __   __  _______  __    _ 
            |       ||  | |  ||       ||  | |  ||       ||  |  | |
            |    _  ||  |_|  ||_     _||  |_|  ||   _   ||   |_| |
            |   |_| ||       |  |   |  |       ||  | |  ||       |
            |    ___||_     _|  |   |  |       ||  |_|  ||  _    |
            |   |      |   |    |   |  |   _   ||       || | |   |
            |___|      |___|    |___|  |__| |__||_______||_|  |__|
                     _______  _______  __    _  _______           
                    |       ||       ||  |  | ||       |          
                    |    _  ||   _   ||   |_| ||    ___|          
                    |   |_| ||  | |  ||       ||   | __           
                    |    ___||  |_|  ||  _    ||   ||  |          
                    |   |    |       || | |   ||   |_| |          
                    |___|    |_______||_|  |__||_______|          
    """

    on = True
    color = True
    currentColor = 0
    hexColors = ['a','b','c','d','e','f']

    def setup(this):
        this.tick = 2

    def update(this):
        screen = "\n" * 3
        screen += this.asciiArt3
        if this.on:
            if this.color:
                this.color = False
                this.currentColor +=1
                if this.currentColor ==  len(this.hexColors):
                    this.currentColor = 0
            else:
                this.color = True
            os.system("color 0" + this.hexColors[this.currentColor])
            this.on = False
            text = "PRESS SPACE TO START  "
        else:
            this.on = True
            text = "  "

        btText = "\n" * 4 + " " * int((80 - len(text)) /2)
        btText += text
        this.render(screen+btText)

    def onEvent(this, ch):
        if ch == " ":
            return MultiplayerGameState({'scores':[0,0]})




