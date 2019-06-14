from state import State
import os

class FinalState(State):

    def setup(this):
        pass

    def update(this):
        this.render(" game over "+ this.data)


class MenuState(State):

    p1=0
    p2=0
    x=1
    y=0
    down=True
    right=True
    width = 80
    #bisogna lasciare una riga vuota
    #altrimenti la console va a capo e si perde la prima riga
    height = 23
    paddleHeight = 5
    
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
        if this.x==78:
            this.right=False
            if this.y>this.p2+4 or this.y<this.p2:
                return(FinalState)
        elif this.x==1:
            this.right=True
            if this.y>this.p1+4 or this.y<this.p1:
                return(FinalState)
        if this.right==True:
            this.x+=1
        else:
            this.x-=1
        if this.y==24:
            this.right=False
        elif this.y==0:
            this.down=True
        if this.down==True:
            this.x+=1
        else:
            this.x-=1
    #questa funzione viene chiamata solo una volta, al momento
    #della inizializzazione dello stato
    def setup(this):
        #imposta la velocita di gioco a 20 tick al secondo
        this.tick = 10

    #questa funzione viene chiamata un botto di volte al secondo
    def update(this):
        this.logic()
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
        print(ch)
        if ch == " ":
            return MenuState()




