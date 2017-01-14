from time import sleep
import random
from graphics import *

win = GraphWin('Game Window',800,600)
plyr = Circle(Point(100,300),25)
plyr.draw(win)
plyr.setFill('#ffffff')
scoreText = Text(Point(400,50),'0')
scoreText.setSize(36)
scoreText.draw(win)
highText = Text(Point(465,50),'0')
highText.setSize(36)
highText.draw(win)

def ChangeColour():
    global initializeColour
    global r
    global g
    global b
    global updown
    global updowng
    global updownb
    if initializeColour == 1:
        r = random.randrange(0,256,1)
        g = random.randrange(0,256,1)
        b = random.randrange(0,256,1)
        rgb = color_rgb(r,g,b)
        win.setBackground(rgb)
        initializeColour = 0
    else:
        r = r + updown
        g = g - updowng
        b = b + updownb
        if r > 254 or r < 1:
            updown = updown * -1
        if g > 254 or g < 1 :
            updowng = updowng * -1
        if b > 254 or b < 1:
            updownb = updownb * -1
        rgb = color_rgb(r,g,b)
        win.setBackground(rgb)
def Walls():
    global newWalls
    global wall1
    global wall2
    global wallspeed
    global NATHAN
    py = random.randrange(25,450,1)
    wall1 = Rectangle(Point(850,0),Point(900,py))
    wall1.setFill('#ff0000')
    wall1.draw(win)
    if NATHAN == 1:
        wall2 = Rectangle(Point(850,(py+random.randrange(60,200,1))),Point(900,600))
    else:
        wall2 = Rectangle(Point(850,(py+100)),Point(900,600))
    wall2.setFill('#ff0000')
    wall2.draw(win)
    newWalls = 0
    if wallspeed > -1:
        wallspeed = -2
    wallspeed = wallspeed - 0.5      
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
#               FUNCTIONS END-----------------------REAL GAME START
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
initializeColour = 1
r = 0
g = 0
b = 0
updown = 1
updowng = -1
updownb = 1
TIMETOGO = 1
newWalls = 1
wallgone = 900
wallspeed = -2
score = 0
highscore = 0
NATHAN = 0

while TIMETOGO == 1:
    key = win.checkKey()
    pC = plyr.getCenter()
    pY = pC.getY()
    pX = pC.getX()
    try:
        w1p1 = wall1.getP1()
        w1p2 = wall1.getP2()
        w2p1 = wall2.getP1()
        w2p2 = wall2.getP2()
        w1p1x = w1p1.getX()
        w1p1y = w1p1.getY()
        w1p2x = w1p2.getX()
        w1p2y = w1p2.getY()
        w2p1x = w2p1.getX()
        w2p1y = w2p1.getY()
        w2p2x = w2p2.getX()
        w2p2y = w2p2.getY()
    except:
        pass
    try:
        if key == 'Up' or key == 'w':
            if pY - 25 <= 12:
                pass
            else:
                plyr.move(0,-15)
        if key == 'Down' or key == 's':
            if pY + 25 >= 588:
                pass
            else:
                plyr.move(0,15)
        if key == 'k':
            NATHAN = 1
        elif key == 'l':
            NATHAN = 0
    except:
        pass
    ChangeColour()
    try:
        if pX + 25 >= w1p1x and pX + 25 <= w1p2x and pY + 25 >= w1p1y and pY + 25 <= w1p2y or pX - 25 >= w1p1x and pX - 25 <= w1p2x and pY - 25 >= w1p1y and pY - 25 <= w1p2y or pX + 25 >= w1p1x and pX + 25 <= w1p2x and pY - 25 >= w1p1y and pY - 25 <= w1p2y or pX - 25 >= w1p1x and pX - 25 <= w1p2x and pY + 25 >= w1p1y and pY + 25 <= w1p2y:
            wall1.undraw()
            wall2.undraw()
            wallgone = 900
            newWalls = 1
            score = 0
            scoreText.setText('0')
            wallspeed = -2
        elif pX + 25 >= w2p1x and pX + 25 <= w2p2x and pY + 25 >= w2p1y and pY + 25 <= w2p2y or pX - 25 >= w2p1x and pX - 25 <= w2p2x and pY - 25 >= w2p1y and pY - 25 <= w2p2y or pX + 25 >= w2p1x and pX + 25 <= w2p2x and pY - 25 >= w2p1y and pY - 25 <= w2p2y or pX - 25 >= w2p1x and pX - 25 <= w2p2x and pY + 25 >= w2p1y and pY + 25 <= w2p2y:
            wall1.undraw()
            wall2.undraw()
            wallgone = 900
            newWalls = 1
            score = 0
            scoreText.setText('0')
            wallspeed = -2
    except:
        pass
    if newWalls == 1:
        Walls()
    elif newWalls == 0:
        wall1.move(wallspeed,0)
        wall2.move(wallspeed,0)
        wallgone = wallgone + wallspeed
    if NATHAN == 1:
        wallspeed = random.randrange(-25,0,1)
    if wallgone < 0:
        newWalls = 1
        wall1.undraw()
        wall2.undraw()
        wallgone = 900
        score = score + 1
        scoreText.setText(score)
    if score > highscore:
        highscore = highscore + 1
        highText.setText(highscore)
    time.sleep(0.0166)
    
