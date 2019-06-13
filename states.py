from state import State


class FinalState(State):

    def setup(this):
        pass

    def update(this):
        this.render(" game over "+ this.data)


class MenuState(State):

    #qua inizializzi tutte le variabili che ti servono
    h = 0
    #puoi anche generare metodi personalizzati. è importante però
    #che il primo parametro sia 'this'
    def myMethod(this, a, b):
        return a+b

    #questa funzione viene chiamata solo una volta, al momento
    #della inizializzazione dello stato
    def setup(this):
        print("ciao")

    #questa funzione viene chiamata un botto di volte al secondo
    def update(this):
        #imposta il numero di volte al secondo per cui va chiamata
        #la funzione update. minimo 1 volta al secondo, massimo 999
        this.tick = 10
        if this.h < 20:
            this.h = this.h + 1
        else:
            #return [nome classe] passa ad il prossimo stato
            return FinalState("ciao")
        screen = "\n" * this.h
        screen = screen + "-" * 10
        #questa funzione è tipo print. stampa quello che gli passi
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




