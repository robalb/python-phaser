from state import State


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
    height = 23
    
    def genstr(this,p1,p2,x,y):
        width = this.width
        height = this.height
        a=[]
        b=['.' for i in range(width)]
        b.append('\n')
        st=''
        for i in range (height):
            a.append(b[:])
        for i in range (5):
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
        print("ciao")

    #questa funzione viene chiamata un botto di volte al secondo
    def update(this):
        this.logic()
        screen=this.genstr(this.p1,this.p2,this.x,this.y)
        this.render(screen)

    #questa funzione viene chiamata quando un tasto viene schiacciato
    def onEvent(this, ch):
        print(ch)


class InitialState(State):

    def update(this):
        screen = "---------\n" * 10
        screen = screen + " premi spazio"
        screen = screen + "----------\n" * 10
        this.render(screen)

    def onEvent(this, ch):
        print(ch)
        if ch == " ":
            return MenuState()




