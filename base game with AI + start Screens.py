#base game with AI

from time import sleep
from cmu_112_graphics import *
import copy
import random
from typing import List
from collections import deque

#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#moveDotWithArrowsAndBounds

#https://pynative.com/python-random-choice/
#112 TA's

#https://en.wikipedia.org/wiki/Minimum_spanning_tree
#https://www.cs.cmu.edu/~112/notes/notes-oop-part2.html




def appStarted(app):
    app.gameOn = False
    app.instruct = False
    app.score = 0
    app.highScores = []
    app.playerX = (app.width/4)
    app.playerY = (app.height/2)
    app.playerR = 20
    app.holding = False
    # app.ai = EnemyAI(object)
    app.customerColors = ["red", "green", "light blue", "orange", "cyan",
    "red", "green", "light blue", "orange", "cyan", "red", "green",
    "light blue", "orange", "cyan", "red", "green", "light blue", "orange",
    "cyan", "red", "green", "light blue", "orange", "cyan", "red", "green",
    "light blue", "orange", "cyan"]
    app.skin = "white"
    app.chosenPlate = []
    app.assembledPlate = []
    app.correctedPlate = []
    app.Plate = []
    app.plate1 = [("light green", "yellow"), ("light green", "yellow"), ("pink", "yellow"),
    ("light yellow", "yellow")]
    app.plate2 = [("light yellow", "yellow"), ("pink", "yellow"),
    ("light green", "yellow"), ("pink", "yellow")]
    app.plate3 = [("light yellow", "yellow"), ("light green", "yellow"), 
    ("pink", "yellow"), ("light yellow", "yellow")]
    #tuple of 2 x0,y0,x1,y1 coords
    app.pcounterTopCoords = [((app.width/4) - 100, (app.height/2) + 50, 
            (app.width/4) + 100, (app.height/2) + 100), ((app.width/4) - 100, 
            (app.height/2) - 100, (app.width/4) + 100, (app.height/2) - 50) ]
    app.serveTableCoords = [((app.width/2) - (app.width/2 - 30), (app.height/2) - 150, (app.width/2) - (app.width/2 - 100),
            (app.height/2) + 150)]
    app.ticketCoords = [((app.width/2) - (app.width/2 - 50), (app.height/2) - 200,
            (app.width/2) - (app.width/2 - 140), (app.height/2) - 80)]
    app.stoveTopCoords = [((app.width/4) - 150, app.height - 50, 
            (app.width/4) - 50, app.height - 5)]
    app.cuttingBoardCoords = [((app.width/4) + 40, (app.height/2) - 60, 
            (app.width/4) + 90 ,(app.height/2) - 90)]
    app.meatFridgeCoords = [((app.width/2) - 80, (app.height/2) - 175, 
            (app.width/2) - 10, (app.height/2) - 75)]
    app.doughBoxCoords = [(app.width/2 - 80, (app.height/2) - 40,
            app.width/2 - 10, app.height/2 + 40)]
    app.veggFridgeCoords = [(app.width/2 - 80, (app.height/2) + 80,
            app.width/2 - 10, (app.height/2) + 180)]
    app.ovenCoords = [((app.width/4) + 30, app.height - 50, 
            (app.width/4) + 130, app.height - 5)]        
    app.trashCoords = [((app.width/2) - 60, (app.height) - 35, 
            (app.width/2) - 10, app.height - 10)]
    app.plateCoords = [(((app.width/2) - (app.width/2 - 50)),
            (app.height/2) + 100, ((app.width/2) - (app.width/2 - 90)), 
            (app.height/2) + 140)]
    app.scoreBoardCoords = [(app.width/2 - 100, (app.height - app.height) + 50,
            app.width/2 - 10, (app.height - app.height) + 100)]
    app.customerLineCoords = [((app.width/2) - (app.width/2 - 5), 
            (app.height/2) - 280,  (app.width/2) - (app.width/2 - 150),
            (app.height/2) - 210)]
    app.pfoodCoords = []#[(cx,cy,color,outline)]
    # app.timerDelay = 1
    app.timerDelay = 600
    # app.timerDelay = 300

    app.gameOver = False
    app.timer = 260

    ######################
    app.aiScore = 0
    app.score = 0
    app.targetCoords = []
    app.rows = 30
    app.cols = 30
    app.aiFoodCoords = []
    app.cellSize = 35
    app.floorColor = "light grey"
    app.echosenPlate = []
    app.enemyX = ((app.width) - (app.width/4)) - (35/4) - 2
    app.enemyY = (app.height/2) - (35/2) + 7
    app.enemyR = 20
    app.startCoords = [14, 14]
    app.aiboard = [([app.floorColor] * app.cols) for _ in range(app.rows)]
    app.dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    app.visitedCoords = [([False] * app.cols) for _ in range(app.rows)]
    app.cuttingBRC = [12,17]
    app.ovenRC = [27,19] 
    app.stoveRC = [27,11] 
    app.meatFRC = [8,26]
    app.doughBRC = [15,26]
    app.veggieFRC = [23, 26]
    app.plateRC = [21,5]
    app.path = []
    app.heldAi = False
    app.done = False
    app.eFoodCoords = [] #[(cx,cy,color,outline)]
    app.plateFoodCoords = []
    app.ecustomerColors = ["red", "green", "light blue", "orange", "cyan",
    "red", "green", "light blue", "orange", "cyan", "red", "green",
    "light blue", "orange", "cyan", "red", "green", "light blue", "orange",
    "cyan", "red", "green", "light blue", "orange", "cyan", "red", "green",
    "light blue", "orange", "cyan"]
    app.ecounterTopCoords = [(((app.width) - (app.width/4)) - 100, (app.height/2) + 50, 
            ((app.width) - (app.width/4)) + 100, (app.height/2) + 100), (((app.width) - (app.width/4)) - 100, 
            (app.height/2) - 100, ((app.width) - (app.width/4)) + 100, (app.height/2) - 50) ]
            #[(300,400,200,400),(200,300,400,300)]
    app.eserveTableCoords = [((app.width/2 + 30), (app.height/2) - 150,
            (app.width/2 + 100), (app.height/2) + 150)]
    app.eticketCoords = [((app.width/2) + (app.width/2 + 50), (app.height/2) - 200,
            (app.width/2) + (app.width/2 + 140), (app.height/2) - 80)]
    app.estoveTopCoords = [(((app.width) - (app.width/4)) - 150, app.height - 50, 
            ((app.width) - (app.width/4)) - 50, app.height - 5)]
    app.ecuttingBoardCoords = [(((app.width) - (app.width/4)) + 40, (app.height/2) - 60, 
            ((app.width) - (app.width/4)) + 90 ,(app.height/2) - 90)]
    app.emeatFridgeCoords = [((app.width) - 80, (app.height/2) - 175, 
            (app.width) - 10, (app.height/2) - 75)]
    app.edoughBoxCoords = [((app.width) - 80, (app.height/2) - 40,
            (app.width) - 10, app.height/2 + 40)]
    app.eveggFridgeCoords = [((app.width) - 80, (app.height/2) + 80,
            (app.width) - 10, (app.height/2) + 180)]
    app.eovenCoords = [(((app.width) - (app.width/4)) + 30, app.height - 50, 
            ((app.width) - (app.width/4)) + 130, app.height - 5)]        
    app.eplateCoords = [(((app.width/2 + 50)),
            (app.height/2) + 100, ((app.width/2 + 90)), 
            (app.height/2) + 140)]
    app.escoreBoardCoords = [((app.width) - 100, (app.height - app.height) + 50,
            (app.width) - 10, (app.height - app.height) + 100)]
    app.ecustomerLineCoords = [((app.width/2 + 5), 
            (app.height/2) - 280, (app.width/2 + 150),
            (app.height/2) - 210)]
    app.etrashCoords = [((app.width) - 60, (app.height) - 35, 
            (app.width) - 10, app.height - 10)]
    Ecollide(app)

#andrew id: ufe, file: Tetris
def initOvercooked(app):
    app.score
    app.instruct = False
    app.gameOver = False
    app.timer = 260
    app.pfoodCoords = []
    app.chosenPlate = []
    app.assembledPlate = []
    app.correctedPlate = []
    app.eFoodCoords = [] #[(cx,cy,color,outline)]
    app.startCoords = [14, 14]
    app.path = []
    app.heldAi = False
    app.done = False
    app.rows = 30
    app.cols = 30
    app.aiFoodCoords = []
    app.cellSize = 35
    app.floorColor = "light grey"
    app.echosenPlate = []
    app.enemyX = ((app.width) - (app.width/4)) - (35/4) - 2
    app.enemyY = (app.height/2) - (35/2) + 7
    app.enemyR = 20
    app.startCoords = [14, 14]
    app.aiboard = [([app.floorColor] * app.cols) for _ in range(app.rows)]
    app.dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    app.visitedCoords = [([False] * app.cols) for _ in range(app.rows)]
    app.cuttingBRC = [12,17]
    app.ovenRC = [27,19] 
    app.stoveRC = [27,11] 
    app.meatFRC = [8,26]
    app.doughBRC = [15,26]
    app.veggieFRC = [23, 26]
    app.plateRC = [21,5]
    app.path = []
    app.heldAi = False
    app.done = False
    app.eFoodCoords = [] #[(cx,cy,color,outline)]
    app.plateFoodCoords = []
    Ecollide(app)

    


    

def generatePath(app):

    path = []

    plate1 = [app.veggieFRC,app.cuttingBRC, app.plateRC, app.veggieFRC,
    app.cuttingBRC, app.plateRC, app.meatFRC, app.stoveRC, app.plateRC, 
    app.doughBRC, app.ovenRC, app.plateRC]

    plate2 = [app.doughBRC, app.ovenRC, app.plateRC, app.meatFRC, app.stoveRC,
    app.plateRC, app.veggieFRC, app.cuttingBRC, app.plateRC,  
    app.doughBRC, app.ovenRC, app.plateRC]

    plate3 = [app.doughBRC, app.ovenRC, app.plateRC, app.veggieFRC,
    app.cuttingBRC, app.plateRC, app.meatFRC, app.stoveRC, app.plateRC, 
    app.doughBRC, app.ovenRC, app.plateRC]

    if app.echosenPlate == app.plate1:
        plate = plate1
    elif app.echosenPlate == app.plate2:
        plate = plate2
    elif app.echosenPlate == app.plate3:
        plate = plate3


    for i in range(0,len(plate)):
        if i < 1:
            start = app.startCoords

        else:
            start = path[-1]

        bfsRes = AiBFS(app.aiboard, start, plate[i])
        if bfsRes != None:
            path.extend(bfsRes)
        if bfsRes == None:
            app.done = True
            app.aiScore += 1
            generateAiPlate(app)
    app.path = path
    


def ifAlreadyHoldingAi(app):
    check = True
    for i in range(len(app.eFoodCoords)):
        cx, cy, color, outline = app.eFoodCoords[i]
        if (cx == app.enemyX and cy == app.enemyY):
            check = False  
    return check

def pickedUpAi(app):
        for i in range(len(app.eFoodCoords)):
            cx, cy, color, outline = app.eFoodCoords[i]
            if ifAlreadyHoldingAi(app) == True:
                if (abs(app.enemyX - cx) <= 25 and
                abs(app.enemyY - cy) <= 25):
                    px = app.enemyX
                    py = app.enemyY
                    app.efoodCoords[i] = (px, py, color, outline)
                    return


def addIngred(app, r, c):
    if r == (app.meatFRC[0]) and c == app.meatFRC[1] - 1 and app.heldAi == False:
        app.eFoodCoords += [(app.enemyX, app.enemyY, "pink", "grey")]
        app.heldAi = not app.heldAi
        if app.holding == True:
            pickedUpAi(app)
    elif (r == (app.doughBRC[0] - 1) or r == app.doughBRC[0]) and (c == app.doughBRC[1] or c == app.doughBRC[1] - 1) and app.heldAi == False:
        app.eFoodCoords += [(app.enemyX, app.enemyY, "light yellow", "grey")]
        app.heldAi = not app.heldAi
        if app.holding == True:
            pickedUpAi(app)
    elif r == (app.veggieFRC[0] - 1) and c == app.veggieFRC[1] and app.heldAi == False:
        app.eFoodCoords += [(app.enemyX, app.enemyY, "light green", "grey")]
        app.heldAi = not app.heldAi
        if app.holding == True:
            pickedUpAi(app)

def process(app, r, c):
    for i in range(len(app.eFoodCoords)):
        cx, cy, color, outline = app.eFoodCoords[i]
        if r == (app.ovenRC[0] - 2) and c == app.ovenRC[1]:
            app.eFoodCoords[i] = cx, cy, color, "yellow"
        if r == app.cuttingBRC[0] and c == app.cuttingBRC[1]:
            app.eFoodCoords[i] = cx, cy, color, "yellow"
        if r == (app.stoveRC[0] - 1) and c == app.stoveRC[1]:
            app.eFoodCoords[i] = cx, cy, color, "yellow"

def nearAiPlate(app):
    if len(app.plateFoodCoords) < 1:
        pass
    for i in range(len(app.eFoodCoords)):
        cx, cy, color, outline = app.eFoodCoords[i]
        x0, y0, x1, y1 = app.eplateCoords[0]
        # if r == app.plateRC[0] and c == app.plateRC[1]:
        if (outline == "yellow" and ((app.enemyX <= x1 + 50)
        and (y0 - 30 <= app.enemyY) and (y1 + 30 >= app.enemyY))):
            px = x1 - 20
            py = y1 - 20
            app.plateFoodCoords = (px, py, color, outline)  
            app.eFoodCoords.pop(i)
            app.heldAi = False
            
def moveAi(app):
    if app.currPath[0] < app.nextPath[0]:
        app.enemyY += (app.cellSize)/1.8
    if app.currPath[0] > app.nextPath[0]:
        app.enemyY -= (app.cellSize)/1.8
    if app.currPath[1] < app.nextPath[1]:
        app.enemyX += (app.cellSize)/1.8
    if app.currPath[1] > app.nextPath[1]:
        app.enemyX -= (app.cellSize)/1.8
    for i in range(len(app.eFoodCoords)):
        cx, cy, color, outline = app.eFoodCoords[i]
        if app.currPath[0] < app.nextPath[0]:
            # app.enemyY += (app.cellSize)/1.8
            if (cx == app.enemyX and 
                cy + 10 == (app.enemyY + ((app.cellSize)/1.8))) : #app.heldAi
                    return
            app.eFoodCoords[i] = (cx,cy+((app.cellSize)/1.8),color, outline)
        if app.currPath[0] > app.nextPath[0]:
            # app.enemyY -= (app.cellSize)/1.8
            
            if (cx == app.enemyX and
                cy + 10 == (app.enemyY)): 
                    return
            app.eFoodCoords[i] = (cx,cy-((app.cellSize)/1.8),color, outline)
        if app.currPath[1] < app.nextPath[1]:
            # app.enemyX += (app.cellSize)/1.8
            
            if (cx == (app.enemyX + ((app.cellSize)/1.8)) and cy + 10 == app.enemyY): #app.heldAi
                    return
            app.eFoodCoords[i] = (cx+((app.cellSize)/1.8),cy,color, outline)
        if app.currPath[1] > app.nextPath[1]:
            # app.enemyX -= (app.cellSize)/1.8
                
            if (app.heldAi == True and 
                cx == (app.enemyX - ((app.cellSize)/1.8)) and cy + 10 == app.enemyY): #app.heldAi
                    return
            app.eFoodCoords[i] = (cx-((app.cellSize)/1.8),cy,color, outline)

def takeStep(app):

    if len(app.path) > 0:
        app.currPath = app.path.pop(0)
        # app.aiboard[app.currPath[0]][app.currPath[1]] = "light blue"
        nearAiPlate(app)
        addIngred(app, app.currPath[0], app.currPath[1])
        process(app, app.currPath[0], app.currPath[1])
            #take off the ingred and add ontop of plate(EASIEST WAY) 

        if app.path:
            app.nextPath = app.path[0]
        else:
            app.echosenPlate = []
            return
        moveAi(app)
    nearChop(app) 
    nearPlate(app)
    if app.chosenPlate == []:
        plate = generatePlate(app)
    nearOven(app)
    nearStove(app)
    nearDoughBox(app)
    nearTrash(app)
    nearVeggieFridge(app)
    nearMeatFridge(app)


def timerFired(app):
    if app.gameOver != True:
        if app.echosenPlate == []:
            generateAiPlate(app)
            generatePath(app)

        if app.done == True:
            generateAiPlate(app)
            generatePath(app)
            app.done == False
            moveAi(app)
        if app.gameOn != False:
            if app.instruct != True:
                takeStep(app)
                if app.timer >= 1:
                    app.timer -= 1
                    if app.timer < 2:
                        app.highScores.append(app.score)
                        list.sort(app.highScores)
                        app.highScores = set(app.highScores)
                        app.highScores = list(app.highScores)

                        
                    if app.timer < 1:
                        print("GAME OVER")
                        app.score = 0
                        
                        app.gameOver = True


#checks to see if a collision occured
def collision(app, x, y):
    allObjs = (app.pcounterTopCoords + app.meatFridgeCoords + 
    app.serveTableCoords + app.stoveTopCoords + app.cuttingBoardCoords + 
    app.veggFridgeCoords + app.doughBoxCoords + app.trashCoords
    + app.ovenCoords)
    for i in range(len(allObjs)):
        x0,y0,x1,y1 = allObjs[i]
        if (x0 <= x <= x1) and (y0 <= y <= y1):
            return False
    return True


def generatePlate(app):
    plate1 = [("light green", "yellow"), ("light green", "yellow"), ("pink", "yellow"),
    ("light yellow", "yellow")]
    plate2 = [("light yellow", "yellow"), ("pink", "yellow"),
    ("light green", "yellow"), ("pink", "yellow")]
    plate3 = [("light yellow", "yellow"), ("light green", "yellow"), 
    ("pink", "yellow"), ("light yellow", "yellow")]
    app.chosenPlate = random.choice([app.plate1, app.plate2, app.plate3])

def generateAiPlate(app):
    plate1 = [("light green", "yellow"), ("light green", "yellow"), ("pink", "yellow"),
    ("light yellow", "yellow")]
    plate2 = [("light yellow", "yellow"), ("pink", "yellow"),
    ("light green", "yellow"), ("pink", "yellow")]
    plate3 = [("light yellow", "yellow"), ("light green", "yellow"), 
    ("pink", "yellow"), ("light yellow", "yellow")]
    app.echosenPlate = random.choice([app.plate1, app.plate2, app.plate3])

def checkTicket(app, plate):
    #put the chosen plate in to a draw
    pickedPlate = plate
    app.correctedPlate = []
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        x0, y0, x1, y1 = app.plateCoords[0]
        if (cx == (x1 - 20) and cy == (y1 - 20)):
            app.assembledPlate += [(cx, cy, color, outline)]
            app.correctedPlate += [(color, outline)]
    if app.correctedPlate == pickedPlate:
        app.score += 1
        return True
    else:
        return False


def ifAlreadyHolding(app):
    check = True
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if (cx == app.playerX and cy == app.playerY):
            check = False  
    return check

def pickedUp(app):
        for i in range(len(app.pfoodCoords)):
            cx, cy, color, outline = app.pfoodCoords[i]
            if ifAlreadyHolding(app) == True:
                if (abs(app.playerX - cx) <= 25 and
                abs(app.playerY - cy) <= 25):
                    px = app.playerX
                    py = app.playerY
                    app.pfoodCoords[i] = (px, py, color, outline)
                    return



def moveLeft(app):
    app.playerX -= 20 
    if (app.playerX - app.playerR < 0):
        app.playerX = app.playerR
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX + 20 and cy == app.playerY:
            if app.holding == True:
                app.pfoodCoords[i] = (cx-20,cy,color,outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerX += 20
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX - 20 and cy == app.playerY:
            if app.holding == True and collision(app, cx, cy) != True:
                app.pfoodCoords[i] = (cx+20, cy, color, outline)

def moveRight(app):
    app.playerX += 20
    if (app.playerX + app.playerR > app.width/2):
        app.playerX = app.width/2 - app.playerR
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX - 20 and cy == app.playerY:
            if app.holding == True:
                app.pfoodCoords[i] = (cx+20,cy,color, outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerX -= 20
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX + 20 and cy == app.playerY:
            if app.holding == True and collision(app, cx, cy) != True:
                app.pfoodCoords[i] = (cx-20, cy, color, outline)

def moveUp(app):
    app.playerY -= 20
    if (app.playerY - app.playerR < 0):
        app.playerY = app.playerR
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX and cy == app.playerY + 20:
            if app.holding == True:
                app.pfoodCoords[i] = (cx,cy-20,color, outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerY += 20
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX and cy == app.playerY - 20:
            if app.holding == True and collision(app, cx, cy) != True:
                app.pfoodCoords[i] = (cx, cy+20, color, outline)

def moveDown(app):
    app.playerY += 20
    if (app.playerY + app.playerR > app.height):
        app.playerY = app.height - app.playerR
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX and cy == app.playerY - 20:
            if app.holding == True:
                app.pfoodCoords[i] = (cx,cy+20,color, outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerY -= 20
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        if cx == app.playerX and cy == app.playerY + 20:
            if app.holding == True and collision(app, cx, cy) != True:
                app.pfoodCoords[i] = (cx, cy-20, color, outline)


# def clearPlate(app):


def nearPlate(app):
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        x0, y0, x1, y1 = app.plateCoords[0]
        #328.0 <= 350 <= 372.0 and 47 + 25 >= 65)
        if (outline == "yellow" and ((cx <= x1 + 30)
        and (y1 + 20 >= cy)) and app.holding == False):
            app.assembledPlate += [(cx, cy, color, outline)]
            px = x1 - 20
            py = y1 - 20
            app.pfoodCoords[i] = (px, py, color, outline)
            
            
def nearMeatFridge(app):
    x0, y0, x1, y1 = app.meatFridgeCoords[0]
    if (y0 <= app.playerY <= y1) and (x0 - 20 <= app.playerX):
        return True
def nearDoughBox(app):
    x0, y0, x1, y1 = app.doughBoxCoords[0]
    if (y0 <= app.playerY <= y1) and (x0 - 20 <= app.playerX):
        return True
def nearVeggieFridge(app):
    x0, y0, x1, y1 = app.veggFridgeCoords[0]
    if (y0 <= app.playerY <= y1) and (x0 - 20 <= app.playerX):
        return True


def nearTrash(app):
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        x0, y0, x1, y1 = app.trashCoords[0]
        if (((y0 <= cy <= y1) and (x0 - 20 <= cx) or
        (x0 <= cx <= x1) and (y0 - 20 >= cy)) 
        and app.holding == False):
            app.pfoodCoords[i] = (cx + 10**10, cy + 10**10,
                                "light grey", "lightgrey")

def nearOven(app):
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        x0, y0, x1, y1 = app.ovenCoords[0]
        if (color == "light yellow" and
        ((x0 <= cx <= x1) and (y0 - 20 <= cy)) 
        and app.holding == False):
            app.pfoodCoords[i] = (cx,cy,color, "yellow")
        
def nearStove(app):
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        x0, y0, x1, y1 = app.stoveTopCoords[0]
        if (color == "pink" and
        ((x0 <= cx <= x1) and (y0 - 20 <= cy)) 
        and app.holding == False):
            app.pfoodCoords[i] = (cx,cy,color, "yellow")

def nearChop(app):
    for i in range(len(app.pfoodCoords)):
        cx, cy, color, outline = app.pfoodCoords[i]
        x0, y0, x1, y1 = app.cuttingBoardCoords[0]
        if (color == "light green" and ((x0 <= cx <= x1) and (y0 + 20 >= cy))
        and app.holding == False):
            app.pfoodCoords[i] = (cx,cy,color, "yellow")

def clearPlate(app):
    copyL = copy.deepcopy(app.pfoodCoords)
    for i in range(len(copyL)):
        x0, y0, x1, y1 = app.plateCoords[0]
        cx, cy, color, outline = app.pfoodCoords[i]
        if (cx == (x1 - 20) and cy == (y1 - 20)):
            tx = cx + 10**10
            ty = cy + 10**10
            app.pfoodCoords[i] = (tx,ty,"light grey", "white")

# hw3.py name: E.j. Ezuma-Ngwu andrew id: ufe
def reverseList(L):
    return L[::-1]

def takeOffOne(app):
    copyL = (copy.deepcopy(app.pfoodCoords))
    rCopyL = reverseList(copyL)
    for i in range(len(copyL)):
        x0, y0, x1, y1 = app.plateCoords[0]
        cx, cy, color, outline = app.pfoodCoords[i]
        if (cx == (x1 - 20) and cy == (y1 - 20)):
            tx = cx + 10**10
            ty = cy + 10**10
            app.pfoodCoords[i] = (tx,ty,"light grey", "white")
            return
            
def keyPressed(app, event):
    if (event.key == "r"):
        app.score = 0
        initOvercooked(app)
        
    elif app.gameOver != True:
        #l for lettuce
        if (event.key == 'i'):
                app.instruct = not app.instruct
        if (event.key == 'Enter'):
            app.gameOn = True
        if (event.key == "v"):
            if nearVeggieFridge(app):
                randX = random.randint(((app.width/4) - 100), ((app.width/4) + 100))
                randY = random.randint(((app.height/2) + 50), ((app.height/2) + 60))
                app.pfoodCoords += [(randX, randY, "light green", "grey")]

        #m for meat
        if (event.key == "m"):
            if nearMeatFridge(app):
                randX = random.randint(((app.width/4) - 100), ((app.width/4) + 100))
                randY = random.randint(((app.height/2) + 50), ((app.height/2) + 60))
                app.pfoodCoords += [(randX, randY, "pink", "grey")]

        #d for dough
        if (event.key == "d"):
            if nearDoughBox(app):
                randX = random.randint(((app.width/4) - 100), ((app.width/4) + 100))
                randY = random.randint(((app.height/2) + 50), ((app.height/2) + 60))
                app.pfoodCoords += [(randX, randY, "light yellow", "grey")]

        if (event.key == "Space"):   
            for i in range(len(app.pfoodCoords)):
                cx, cy, color, outline = app.pfoodCoords[i]
                if (abs(app.playerX - cx) <= 30 and
                abs(app.playerY - cy) <= 30):
                    app.holding = not app.holding
                    if app.holding == True:
                        pickedUp(app)

        if (event.key == 'Left'):
            moveLeft(app)
            
        if (event.key == 'Right'):
            moveRight(app)
        
        if (event.key == 'Up'):
            moveUp(app)
            
        if (event.key == 'Down'):
            moveDown(app)
        if (event.key == 't'):
            takeOffOne(app)
        if (event.key == 'Tab'):

            if checkTicket(app, app.chosenPlate) == True:
                clearPlate(app)
                app.correctedPlate = []
                app.customerColors.pop(0)
            else:
                app.score -= 1

        
def drawSpawnedIngredient(app, canvas):
    r = 15
    for i in range(len(app.pfoodCoords)):
        cx,cy,color,outline = app.pfoodCoords[i]
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, width = 3,
        outline = outline)
def drawCounterTops(app, canvas):
    for i in range(len(app.pcounterTopCoords)):
        x0,y0,x1,y1 = app.pcounterTopCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "brown", outline = "grey",
         width = 4)

def drawTrash(app, canvas):
    for i in range(len(app.trashCoords)):
        x0,y0,x1,y1 = app.trashCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "black", 
        outline = "black", width = 3)
        canvas.create_text(x1 - 25 ,y1 - 20, text= 'TRASH', 
        font='Calibri 8 bold', fill='white')

def drawServeTable(app, canvas):
    for i in range(len(app.serveTableCoords)):
        x0,y0,x1,y1 = app.serveTableCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 3)
        canvas.create_text(x0 + 25 ,y0 + 150, text='Serve Table', angle = 90, 
                font='Calibri 15 bold', fill='white')

def drawVeggieFridge(app, canvas):
    for i in range(len(app.veggFridgeCoords)):
        x0,y0,x1,y1 = app.veggFridgeCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", outline = "grey",
        width = 3)
        canvas.create_text(x1 - 35 ,y0 + 50, text='Veggie Fridge', angle = 270,
        font='Calibri 15 bold', fill='lightgreen', width = 70)

def drawMeatFridge(app, canvas):
    for i in range(len(app.meatFridgeCoords)):
        x0,y0,x1,y1 = app.meatFridgeCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", outline = "grey",
        width = 3)
        canvas.create_text(x1 - 40 ,y1 - 60, text='Meat Fridge', angle = 270,
        font='Calibri 15 bold', fill='pink', width = 70)

def drawDoughBox(app, canvas):
    for i in range(len(app.doughBoxCoords)):
        x0,y0,x1,y1 = app.doughBoxCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "light yellow", 
        outline = "black", width = 3)
        canvas.create_text(x1- 40 ,y1 - 40, text='Dough Box', angle = 270,
        font='Calibri 15 bold', fill='black', width = 70)


def drawCuttingBoard(app, canvas):
    for i in range(len(app.cuttingBoardCoords)):
        x0,y0,x1,y1 = app.cuttingBoardCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", 
        outline = "light blue", width = 3)
        canvas.create_rectangle(x1 - 10, y0 - 5, x1 - 5, y1 + 5, 
        fill = "brown", outline = "light blue", width = 2)
        canvas.create_text(x0+25 ,y0 - 37, text='Cutting Board',
        font='Calibri 10 bold', fill='light grey')

def drawPlate(app, canvas):
    for i in range(len(app.plateCoords)):
        x0, y0, x1, y1 = app.plateCoords[i]
        canvas.create_rectangle(x0-3,y0+3,x1-3,y1+3, fill="light grey", 
        width = 2, outline = "black")
        canvas.create_rectangle(x0,y0,x1,y1, fill="white", width = 2,
        outline = "black")
        canvas.create_text(x0 + 20, y0 -10, text='Plate',
        font='Calibri 10 bold', fill='black')

def drawOven(app, canvas):
    for i in range(len(app.ovenCoords)):
        x0,y0,x1,y1 = app.ovenCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 2)
        canvas.create_text(x0+50 ,y1-5, text='Oven', font='Calibri 10 bold',
        fill='white')

def drawStoveTop(app, canvas):
    for i in range(len(app.stoveTopCoords)):
        x0,y0,x1,y1 = app.stoveTopCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 2)
        canvas.create_oval(x0 + 5, y0 + 5, x0 + 45, y1 - 5, fill = "orange",
        outline = "yellow", width = "2")
        canvas.create_oval(x0 + 55, y0 + 5, x1 - 5, y1 - 5, fill = "orange",
        outline = "yellow", width = "2")
        canvas.create_text(x0+50 ,y1-5, text='Stove', font='Calibri 10 bold',
         fill='white')

#non objects         
#################

def drawTicket(app, canvas):
    for i in range(len(app.ticketCoords)):
        x0,y0,x1,y1 = app.ticketCoords[i]
        
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", outline = "black",
        width = 3)
        canvas.create_text(x0 + 45 ,y0 + 10, text='Ticket',
        font='Calibri 20 bold', fill='black')
        if app.chosenPlate == app.plate1:
            canvas.create_rectangle(x0,y0,x1,y1, fill = "white", 
            outline = "black", width = 3)
            canvas.create_text(x0 + 45 ,y0 + 10, text='Ticket',
            font='Calibri 20 bold', fill='black')
            canvas.create_text(x0 + 45 ,y0 + 70,  
            text="""CHICKEN CAESAR SALAD
            1 Chopped Veggie,
            1 Chopped Veggie,
            1 Seared Meat,
            1 Baked Dough""",
            font='Calibri 6 bold', fill='black', width = 85)
        elif app.chosenPlate == app.plate2:
            canvas.create_rectangle(x0,y0,x1,y1, fill = "white", 
            outline = "black", width = 3)
            canvas.create_text(x0 + 45 ,y0 + 10, text='Ticket',
            font='Calibri 20 bold', fill='black')
            canvas.create_text(x0 + 45 ,y0 + 70, 
            text="""CHICKEN SANDWICH WITH A SIDE OF NUGGETS
            1 Baked Dough,
            1 Seared Meat,
            1 Chopped Veggie,
            1 Seared Meat""",
            font='Calibri 6 bold', fill='black', width = 85)
        elif app.chosenPlate == app.plate3:
            canvas.create_rectangle(x0,y0,x1,y1, fill = "white", 
            outline = "black", width = 3)
            canvas.create_text(x0 + 45 ,y0 + 10, text='Ticket',
            font='Calibri 20 bold', fill='black')
            canvas.create_text(x0 + 45 ,y0 + 70, 
            text="""BURGER AND FRIES
            1 Baked Dough, 
            1 Chopped Veggie,
            1 Seared Meat, 
            1 Baked Dough""",
            font='Calibri 6 bold', fill='black', width = 85)
        if app.correctedPlate == app.chosenPlate:
            canvas.create_rectangle(x0,y0,x1,y1, fill = "white", outline = "black",
            width = 3)
            canvas.create_text(x0 + 45 ,y0 + 10, text='Ticket',
            font='Calibri 20 bold', fill='black')
def drawStart(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan")
    canvas.create_text(app.width/2, app.height/2 - 200, fill = "Yellow",
    font = "Arial 70 bold", text = "OverCooked2?")
    canvas.create_text(app.width/2, app.height/2, fill = "blue",
    font = "Euphemia 30 bold", width = app.width/2 + 200,
    text = "Press Enter to Begin!")
   
def drawInstructions(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/2 - 300, app.height/2 - 250, app.width/2 + 300, app.height/2 - 150, fill = "light yellow", outline = "light green", width = 10)
    canvas.create_text(app.width/2, app.height/2 - 200, fill = "black",
    font = "Vani 50 bold", text = "Instructions!")

    canvas.create_rectangle(app.width/2 - 580, app.height/2 - 125, app.width/2 + 580, app.height - 25, fill = "pink", outline = "light green", width = 10)
    canvas.create_text((app.width) - 600, app.height/2 + 75, fill = "black",
    font = "Calibri 20 bold", width = app.width - 100,
    text = """1. You are playing on the left of the screen and control the player with the arrow keys

2. You pick up and drop with the Space Bar

3. Use the ticket and you will see all the ingredients needed for the plate.

4. You need to go to the different fridges and press d for dough, m for meat, and v for veggies IN TICKET ORDER.

5. You should pick up and drag the ingredients to the correct places to process/cook them.

6. Once you have the ingredient processed, drop it near the plate.

7. Once you think you have the correct order, press Tab to check and if you don't get it right you can toss the top most ingredient with t.

8. If you have too many ingredients spawned, you can drop them near the left of the trash for disposal.
    """)
def drawGameOver(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light grey")
    canvas.create_text(app.width/2, app.height/2 - 200, fill = "orange",
    font = "Calibri 35 bold", text = "Game Over!")
    for i in range(len(app.highScores)):
    #MAIN HIGHSCORES
        scores = reverseList(app.highScores)
        canvas.create_text(app.width - 100, (app.height/2 - 250), fill = "blue",
    font = "Calibri 25 bold",
    text = f"HIGHSCORES:")
    #SCORES
        canvas.create_text(app.width - 100, (app.height/2 - 250) + (15*(i+2)), fill = "blue",
    font = "Calibri 15 bold",
    text = f"{scores[i]}")
    if app.score >= 2:
        canvas.create_text(app.width/2, app.height/2, fill = "blue",
    font = "Calibri 20 bold", width = app.width/2 + 200,
    text = f"Your Score was: {app.score} Meaning You WON! Press r to Restart")

    else: 
        canvas.create_text(app.width/2, app.height/2, fill = "blue",
    font = "Calibri 20 bold", width = app.width/2 + 200,
    text = f"Your Score was: {app.score}, Meaning You Lost Unfortunately! Press r to Restart")

def drawScore(app, canvas):
    for i in range(len(app.scoreBoardCoords)):
        x0, y0, x1, y1 = app.scoreBoardCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "red", outline = "orange",
        width = 3)
        canvas.create_text(x0+50 ,y0+20, text= f'Plates Made = {app.score}',
        font='Arial 15', fill='white', width = 80)

def drawCustomers(app, canvas):
    for i in range(len(app.customerLineCoords)):
        x0, y0, x1, y1 = app.customerLineCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "purple", 
        outline = "light yellow", width = 3)
        canvas.create_text(x0+55 ,y0-10, text= 'Customer Line',
        font='Calibri 15 bold', fill='black')
        for i in range(len(app.customerColors)):
            r = 12

            #3rd customer
            canvas.create_rectangle(x0 + 30,y0 + 20, x0 + 50, y1 - 20, fill = app.customerColors[i+2],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 30, y0, x0 + 50, y0 + 20, fill = app.skin)
            #2nd customer
            canvas.create_rectangle(x0 + 70,y0 + 20, x0 + 90, y1 - 20, fill = app.customerColors[i+1],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 70, y0, x0 + 90, y0 + 20, fill = app.skin)
            #1st customer
            canvas.create_rectangle(x0 + 110,y0 + 20, x0 + 130,y1 - 20, fill = app.customerColors[i],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 110, y0, x0 + 130, y0 + 20, fill = app.skin)
            return

def drawTimer(app, canvas):
    for i in range(len(app.customerLineCoords)):
        x0, y0, x1, y1 = app.customerLineCoords[i]
        canvas.create_text(app.width/2 - 50, 30, text= f'Time: {app.timer}',
        font='Calibri 15 bold', fill='black')



###########################
# AI FUNCTIONS
#used https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
# https://www.educative.io/edpresso/how-to-implement-a-queue-in-python




class Node:
    # (r, c) represents coords of a cell in the board
    def __init__(self, r, c, root=None):
        self.r = r
        self.c = c
        self.root = root
    def __repr__(self):
        return str((self.r, self.c))
def isValid(board,r, c, n):
    return (0 <= r < n) and (0 <= c < n) and board[r][c] == "light grey"

def getPath(node):
    path = [(node.root.r,node.root.c)]
    while node.root:
        path.append((node.root.r,node.root.c))
        node = node.root
    path.reverse()
    return path






def AiBFS(board, startCoords, targetCoords):

    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    n = len(board)
    r = startCoords[0]
    c = startCoords[1]


    q = []
    src = Node(r, c)
    q.append(src)

    visited = set()
    visited.add((r,c))

    while q:
        currNode = q.pop(0)
        r = currNode.r
        c = currNode.c

        if [r,c] == targetCoords:
            path = getPath(currNode)
            return path
        
        for k in range(4):

            newr = r + row[k]
            newc = c + col[k]

            if isValid(board,newr,newc,n):

                nextNode = Node(newr,newc,currNode)
                if (newr,newc) not in visited:
                    q.append(nextNode)
                    visited.add((newr,newc))
    return None


#from: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.height/2
    gridHeight = app.height 
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = col * cellWidth * 2
    x1 = (col+1) * cellWidth * 2
    y0 = row * cellHeight
    y1 = (row+1) * cellHeight
    return (x0, y0, x1, y1)

def drawCell(app, canvas, cellRow, cellCol):
    (x0, y0, x1, y1) = getCellBounds(app, cellRow, cellCol)
    # app.cellCoords += 
    # text = app.aiboard[cellRow][cellCol]
    canvas.create_rectangle(x0 + app.width/2, y0, x1 + app.width/2, y1, 
    fill = app.aiboard[cellRow][cellCol],  
                            outline = "black")
    
    # app.cellCoords += []
def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, canvas, row, col)

def Ecollide(app):
    #NO PASS = "red"
    #meat fridge = "orange"
    #dough = "brown"
    #veggie = "green"
    #stove = "grey"
    #oven = "black"
    #cuutingB = "blue"
    #plate = "white"

    #Top counter
    for row in range(10,12):
        for col in range(10,20):
            app.aiboard[row][col] = "red"
    #Bottom counter
    for row in range(18,20):
        for col in range(10,20):
            app.aiboard[row][col] = "red"
    #serve table
    for row in range(9,22):
        for col in range(2,5):
            app.aiboard[row][col] = "red"
    #meat fridge
    for row in range(7,11):
        for col in range(27,30):
            app.aiboard[row][col] = "orange"
    #dough box
    for row in range(13,17):
        for col in range(27,30):
            app.aiboard[row][col] = "brown"
    #veggie fridge
    for row in range(20,24):
        for col in range(27,30):
            app.aiboard[row][col] = "green"
    #oven    
    for row in range(28,30):
        for col in range(17,21):
            app.aiboard[row][col] = "black"
    #stove top
    for row in range(28,30):
        for col in range(9,13):
            app.aiboard[row][col] = "grey"
    #cuttingB
    for row in range(11,12):
        for col in range(17,20):
            app.aiboard[row][col] = "blue"
    #plate
    for row in range(20,22):
        for col in range(3,5):
            app.aiboard[row][col] = "white"

    
# def fdrawCell(app, canvas, cellRow, cellCol):
#     (x0, y0, x1, y1) = getCellBounds(app, cellRow, cellCol)
#     canvas.create_rectangle(x0, y0, x1, y1, fill = app.aiboard[cellRow][cellCol], 
#                             outline = "green")
# def fdrawBoard(app, canvas):
#     for row in range(app.rows):
#         for col in range(app.cols):
#             fdrawCell(app, canvas, row, col)

def edrawSpawnedIngredient(app, canvas):
    r = 15
    for i in range(len(app.eFoodCoords)):
        cx,cy,color,outline = app.eFoodCoords[i]
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, width = 3,
        outline = outline)

def edrawCounterTops(app, canvas):
    for i in range(len(app.ecounterTopCoords)):
        x0,y0,x1,y1 = app.ecounterTopCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "brown", outline = "grey",
         width = 4)

def edrawServeTable(app, canvas):
    for i in range(len(app.eserveTableCoords)):
        x0,y0,x1,y1 = app.eserveTableCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 3)
        canvas.create_text(x0 + 25 ,y0 + 150, text='Serve Table', angle = 90, 
                font='Calibri 15 bold', fill='white')

def edrawVeggieFridge(app, canvas):
    for i in range(len(app.eveggFridgeCoords)):
        x0,y0,x1,y1 = app.eveggFridgeCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", outline = "grey",
        width = 3)
        canvas.create_text(x1 - 35 ,y0 + 50, text='Veggie Fridge', angle = 270,
        font='Calibri 15 bold', fill='lightgreen', width = 70)

def edrawMeatFridge(app, canvas):
    for i in range(len(app.emeatFridgeCoords)):
        x0,y0,x1,y1 = app.emeatFridgeCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", outline = "grey",
        width = 3)
        canvas.create_text(x1 - 40 ,y1 - 60, text='Meat Fridge', angle = 270,
        font='Calibri 15 bold', fill='pink', width = 70)

def edrawDoughBox(app, canvas):
    for i in range(len(app.edoughBoxCoords)):
        x0,y0,x1,y1 = app.edoughBoxCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "light yellow", 
        outline = "black", width = 3)
        canvas.create_text(x1- 40 ,y1 - 40, text='Dough Box', angle = 270,
        font='Calibri 15 bold', fill='black', width = 70)


def edrawCuttingBoard(app, canvas):
    for i in range(len(app.ecuttingBoardCoords)):
        x0,y0,x1,y1 = app.ecuttingBoardCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", 
        outline = "light blue", width = 3)
        canvas.create_rectangle(x1 - 10, y0 - 5, x1 - 5, y1 + 5, 
        fill = "brown", outline = "light blue", width = 2)
        canvas.create_text(x0+25 ,y0 - 37, text='Cutting Board',
        font='Calibri 10 bold', fill='light grey')

def edrawPlate(app, canvas):
    for i in range(len(app.eplateCoords)):
        x0, y0, x1, y1 = app.eplateCoords[i]
        canvas.create_rectangle(x0-3,y0+3,x1-3,y1+3, fill="light grey", 
        width = 2, outline = "black")
        canvas.create_rectangle(x0,y0,x1,y1, fill="white", width = 2,
        outline = "black")
        canvas.create_text(x0 + 20, y0 -10, text='Plate',
        font='Calibri 10 bold', fill='black')
        r = 15

        if app.plateFoodCoords != []:
            cx,cy,color,outline = app.plateFoodCoords
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, width = 3,
            outline = outline)    
        
def edrawOven(app, canvas):
    for i in range(len(app.eovenCoords)):
        x0,y0,x1,y1 = app.eovenCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 2)
        canvas.create_text(x0+50 ,y1-5, text='Oven', font='Calibri 10 bold',
        fill='white')

def edrawStoveTop(app, canvas):
    for i in range(len(app.estoveTopCoords)):
        x0,y0,x1,y1 = app.estoveTopCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 2)
        canvas.create_oval(x0 + 5, y0 + 5, x0 + 45, y1 - 5, fill = "orange",
        outline = "yellow", width = "2")
        canvas.create_oval(x0 + 55, y0 + 5, x1 - 5, y1 - 5, fill = "orange",
        outline = "yellow", width = "2")
        canvas.create_text(x0+50 ,y1-5, text='Stove', font='Calibri 10 bold',
         fill='white')

def edrawTrash(app, canvas):
    for i in range(len(app.etrashCoords)):
        x0,y0,x1,y1 = app.etrashCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "black", 
        outline = "black", width = 3)
        canvas.create_text(x1 - 25 ,y1 - 20, text= 'TRASH', 
        font='Calibri 8 bold', fill='white')

def edrawCustomers(app, canvas):
    for i in range(len(app.ecustomerLineCoords)):
        x0, y0, x1, y1 = app.ecustomerLineCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "purple", 
        outline = "light yellow", width = 3)
        canvas.create_text(x0+55 ,y0-10, text= 'Customer Line',
        font='Calibri 15 bold', fill='black')
        for i in range(len(app.ecustomerColors)):
            r = 12

            #3rd customer
            canvas.create_rectangle(x0 + 30,y0 + 20, x0 + 50, y1 - 20, fill = app.ecustomerColors[i+2],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 30, y0, x0 + 50, y0 + 20, fill = app.skin)
            #2nd customer
            canvas.create_rectangle(x0 + 70,y0 + 20, x0 + 90, y1 - 20, fill = app.ecustomerColors[i+1],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 70, y0, x0 + 90, y0 + 20, fill = app.skin)
            #1st customer
            canvas.create_rectangle(x0 + 110,y0 + 20, x0 + 130,y1 - 20, fill = app.ecustomerColors[i],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 110, y0, x0 + 130, y0 + 20, fill = app.skin)
            return
def edrawScore(app, canvas):
    for i in range(len(app.escoreBoardCoords)):
        x0, y0, x1, y1 = app.escoreBoardCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "red", outline = "orange",
        width = 3)
        canvas.create_text(x0+50 ,y0+20, text= f'Plates Made = {app.aiScore}',
        font='Arial 15', fill='white', width = 80)

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width/2, app.height, fill = "light grey")
    drawBoard(app, canvas)
    # fdrawBoard(app,canvas)
    drawCounterTops(app, canvas)
    drawServeTable(app, canvas)
    drawStoveTop(app,canvas)
    drawOven(app, canvas)
    drawCuttingBoard(app,canvas)
    drawDoughBox(app, canvas)
    drawMeatFridge(app, canvas)
    drawVeggieFridge(app, canvas)
    drawTrash(app, canvas)
    drawPlate(app, canvas)
    drawScore(app, canvas)
    drawCustomers(app, canvas)
    drawTimer(app, canvas)

####
#COMMENT ALL BELOW Up To edrawScore TO SEE THE GRID
    canvas.create_rectangle(app.width/2, 0, app.width, app.height, fill = "light grey")

    edrawCounterTops(app, canvas)
    
    edrawCustomers(app, canvas)

    edrawServeTable(app, canvas)
    edrawTrash(app, canvas)
    edrawPlate(app, canvas)
    edrawStoveTop(app,canvas)
    edrawOven(app, canvas)
    edrawCuttingBoard(app,canvas)
    edrawDoughBox(app, canvas)
    edrawMeatFridge(app, canvas)
    edrawVeggieFridge(app, canvas)
    edrawScore(app, canvas)
    canvas.create_text(app.width/4, app.height/10, 
    text="Press i For Help!",
    font='Calibri 20',
    fill='purple', width = 300)
    canvas.create_text(app.width - (app.width/4), app.height/10, 
    text="RIVAL COOK",
    font='Calibri 30 italic',
    fill='grey', width = 300)
    canvas.create_oval(app.playerX-app.playerR, app.playerY-app.playerR,
                       app.playerX+app.playerR, app.playerY+app.playerR,
                       fill='cyan')
    canvas.create_oval(app.enemyX-app.enemyR, app.enemyY-app.enemyR,
                       app.enemyX+app.enemyR, app.enemyY+app.enemyR,
                       fill='purple')
    
    drawSpawnedIngredient(app, canvas)
    edrawSpawnedIngredient(app, canvas)
    drawTicket(app, canvas)
    drawStart(app, canvas)

    if app.gameOver == True:
        drawGameOver(app, canvas)
    elif app.gameOver != True:

        if app.gameOn == True:
            canvas.create_rectangle(0, 0, app.width/2, app.height, fill = "light grey")
            drawBoard(app, canvas)
            # fdrawBoard(app,canvas)
            drawCounterTops(app, canvas)
            drawServeTable(app, canvas)
            drawStoveTop(app,canvas)
            drawOven(app, canvas)
            drawCuttingBoard(app,canvas)
            drawDoughBox(app, canvas)
            drawMeatFridge(app, canvas)
            drawVeggieFridge(app, canvas)
            drawTrash(app, canvas)
            drawPlate(app, canvas)
            drawScore(app, canvas)
            drawCustomers(app, canvas)
            drawTimer(app, canvas)
        ####
        #COMMENT ALL BELOW Up To edrawScore TO SEE THE GRID
            canvas.create_rectangle(app.width/2, 0, app.width, app.height, fill = "light grey")

            edrawCounterTops(app, canvas)
            
            edrawCustomers(app, canvas)

            edrawServeTable(app, canvas)
            edrawTrash(app, canvas)
            edrawPlate(app, canvas)
            edrawStoveTop(app,canvas)
            edrawOven(app, canvas)
            edrawCuttingBoard(app,canvas)
            edrawDoughBox(app, canvas)
            edrawMeatFridge(app, canvas)
            edrawVeggieFridge(app, canvas)
            edrawScore(app, canvas)
            canvas.create_text(app.width/4, app.height/10, 
            text="Press i For Help!",
            font='Calibri 20',
            fill='purple', width = 300)
            canvas.create_text(app.width - (app.width/4), app.height/10, 
            text="RIVAL COOK",
            font='Calibri 30 italic',
            fill='grey', width = 300)
            canvas.create_oval(app.playerX-app.playerR, app.playerY-app.playerR,
                            app.playerX+app.playerR, app.playerY+app.playerR,
                            fill='cyan')
            canvas.create_oval(app.enemyX-app.enemyR, app.enemyY-app.enemyR,
                            app.enemyX+app.enemyR, app.enemyY+app.enemyR,
                            fill='purple')
            
            drawSpawnedIngredient(app, canvas)
            edrawSpawnedIngredient(app, canvas)
            # drawSpawnedAIIngredient(app, canvas)
            drawTicket(app, canvas)
            if app.instruct != False:
                drawInstructions(app, canvas)
            if app.instruct != True:
                canvas.create_rectangle(0, 0, app.width/2, app.height, fill = "light grey")
                drawBoard(app, canvas)
                # fdrawBoard(app,canvas)
                drawCounterTops(app, canvas)
                drawServeTable(app, canvas)
                drawStoveTop(app,canvas)
                drawOven(app, canvas)
                drawCuttingBoard(app,canvas)
                drawDoughBox(app, canvas)
                drawMeatFridge(app, canvas)
                drawVeggieFridge(app, canvas)
                drawTrash(app, canvas)
                drawPlate(app, canvas)
                drawScore(app, canvas)
                drawCustomers(app, canvas)
                drawTimer(app, canvas)
            ####
            #COMMENT ALL BELOW Up To edrawScore TO SEE THE GRID
                canvas.create_rectangle(app.width/2, 0, app.width, app.height, fill = "light grey")

                edrawCounterTops(app, canvas)
                
                edrawCustomers(app, canvas)

                edrawServeTable(app, canvas)
                edrawTrash(app, canvas)
                edrawPlate(app, canvas)
                edrawStoveTop(app,canvas)
                edrawOven(app, canvas)
                edrawCuttingBoard(app,canvas)
                edrawDoughBox(app, canvas)
                edrawMeatFridge(app, canvas)
                edrawVeggieFridge(app, canvas)
                edrawScore(app, canvas)
                canvas.create_text(app.width/4, app.height/10, 
                text="Press i For Help!",
                font='Calibri 20',
                fill='purple', width = 300)
                canvas.create_text(app.width - (app.width/4), app.height/10, 
                text="RIVAL COOK",
                font='Calibri 30 italic',
                fill='grey', width = 300)
                canvas.create_oval(app.playerX-app.playerR, app.playerY-app.playerR,
                                app.playerX+app.playerR, app.playerY+app.playerR,
                                fill='cyan')
                canvas.create_oval(app.enemyX-app.enemyR, app.enemyY-app.enemyR,
                                app.enemyX+app.enemyR, app.enemyY+app.enemyR,
                                fill='purple')
                
                drawSpawnedIngredient(app, canvas)
                edrawSpawnedIngredient(app, canvas)
                drawTicket(app, canvas)
        
runApp(width=1200, height=600)