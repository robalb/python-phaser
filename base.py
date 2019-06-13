import os
import time
import msvcrt

arrows = {
    72: "up",
    80: "down",
    75: "left",
    77: "right"
    }



class Ship:
    def __init__(this):
        this.x = 0
        this.y = 0
        this.ship = "@"
        this.vel = 1
        #the ship 'owned' bullet
        this.bullet = False

    def move(this, direction):
        if direction == "down":
            this.y = this.y + this.vel
        elif direction == "up" and this.y > 0:
            this.y = this.y - this.vel
        elif direction == "left" and this.x > 0:
            this.x = this.x - this.vel
        elif direction == "right":
            this.x = this.x + this.vel
        this._render()

    def rotate(this):
        print("rotated")
        this.vel = this.vel + 1

    def shoot(this):
        os.system("color 4f")
        time.sleep(0.1)
        os.system("color 0f")





    def _render(this):
        os.system("cls")
        topOffset = 0
        leftOffset = 0
        secTopOffset = 0
        if(this.bullet):
            secTopOffset = this.bullet.y
            topOffset = "\n" * secTopOffset
            leftOffset = " " * this.bullet.x
            print(this.bullet.shape)

        topOffset = "\n" * (this.y - secTopOffset)
        leftOffset = " " * this.x
        print(topOffset + leftOffset + this.ship)

ship = Ship()

def inputHandler(ch):
    if ch == " ":
        game.start()
    if ch in arrows.values():
        game.move(ch)






#main input listener loop
done = False
arrow = False
while not done:
    if msvcrt.kbhit():
        c = msvcrt.getch()
        asc = ord(c)
        if arrow:
            arrow = False
            # print("arrow",arrows[asc])
            inputHandler(arrows[asc])
        else:
            if asc == 224:
                arrow = True
            else:
                # print(chr(asc))
                inputHandler(chr(asc))



