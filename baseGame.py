from cmu_112_graphics import *

import copy
import random

#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#moveDotWithArrowsAndBounds

#https://pynative.com/python-random-choice/
#112 TA's

#make a boolean variable in the foodCoords
# if nearChop == True in boolean change that boolean to true
#and then if the boolean is true in drawIngredients outline = "yellow"

def appStarted(app):
    app.score = 0
    app.playerX = (app.width/2)
    app.playerY = (app.height/2)
    app.playerR = 20
    app.holding = False
    app.customerColors = ["red", "green", "light blue", "orange", "cyan",
    "red", "green", "light blue", "orange", "cyan", "red", "green",
    "light blue", "orange", "cyan", "red", "green", "light blue", "orange",
    "cyan", "red", "green", "light blue", "orange", "cyan", "red", "green",
    "light blue", "orange", "cyan"]
    app.skin = "white"
    app.chosenPlate = []
    app.assembledPlate = []
    app.correctedPlate = []
    app.plate1 = [("light green", "yellow"), ("light green", "yellow"), ("pink", "yellow"),
    ("light yellow", "yellow")]
    app.plate2 = [("light yellow", "yellow"), ("pink", "yellow"),
    ("light green", "yellow"), ("pink", "yellow")]
    app.plate3 = [("light yellow", "yellow"), ("light green", "yellow"), 
    ("pink", "yellow"), ("light yellow", "yellow")]
    #tuple of 2 x0,y0,x1,y1 coords
    app.counterTopCoords = [((app.width/2) - 100, (app.height/2) + 50, 
            (app.width/2) + 100, (app.height/2) + 100), ((app.width/2) - 100, 
            (app.height/2) - 100, (app.width/2) + 100, (app.height/2) - 50) ]
            #[(300,400,200,400),(200,300,400,300)]
    app.serveTableCoords = [((app.width) - (app.width - 30), (app.height/2) - 150, (app.width/2) - 200,
            (app.height/2) + 150)]
    app.ticketCoords = [((app.width) - (app.width - 50), (app.height/2) - 200,
            (app.width) - (app.width - 140), (app.height/2) - 80)]
    app.stoveTopCoords = [((app.width/2) - 150, app.height - 50, 
            (app.width/2) - 50, app.height - 5)]
    app.cuttingBoardCoords = [((app.width/2) + 40, (app.height/2) - 60, 
            (app.width/2) + 90 ,(app.height/2) - 90)]
    app.meatFridgeCoords = [((app.width) - 80, (app.height/2) - 175, 
            (app.width) - 10, (app.height/2) - 75)]
    app.doughBoxCoords = [(app.width - 80, (app.height/2) - 40,
            app.width - 10, app.height/2 + 40)]
    app.veggFridgeCoords = [(app.width - 80, (app.height/2) + 80,
            app.width - 10, (app.height/2) + 180)]
    app.ovenCoords = [((app.width/2) + 30, app.height - 50, 
            (app.width/2) + 130, app.height - 5)]        
    app.trashCoords = [((app.width) - 60, (app.height) - 35, 
            (app.width) - 10, app.height - 10)]
    app.plateCoords = [(((app.width) - (app.width - 50)),
            (app.height/2) + 100, ((app.width) - (app.width - 90)), 
            (app.height/2) + 140)]
    app.scoreBoardCoords = [(app.width - 100, (app.height - app.height) + 50,
            app.width - 10, (app.height - app.height) + 100)]
    app.customerLineCoords = [((app.width) - (app.width - 5), 
            (app.height/2) - 280,  (app.width) - (app.width - 150),
            (app.height/2) - 210)]
    app.foodCoords = []#[(cx,cy,color,outline)]
    app.timerDelay = 1000
    app.gameOver = False
    app.timer = 60
    
#andrew id: ufe, file: Tetris
def initOvercooked(app):
    app.gameOver = False
    app.timer = 5
    app.foodCoords = []
    app.chosenPlate = []
    app.assembledPlate = []
    app.correctedPlate = []

def takeStep(app):
    if app.timer >= 1:
        app.timer -= 1
        if app.timer < 1:
            print("GAME OVER")
            app.gameOver = True
    # print(app.plateCoords)
    # print(app.chosenPlate)
    # print(app.correctedPlate)
    if app.chosenPlate == []:
        generatePlate(app)
    nearChop(app)
    nearPlate(app)
    # app.counter += 100 
    # if app.counter == app.counter + 500:
    nearOven(app)
    nearStove(app)
    nearDoughBox(app)
    nearTrash(app)
    nearVeggieFridge(app)
    nearMeatFridge(app)

def timerFired(app):
    if app.gameOver != True:
        return takeStep(app)

#checks to see if a collision occured
def collision(app, x, y):
    allObjs = (app.counterTopCoords + app.meatFridgeCoords + 
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

def checkTicket(app, plate):
    #put the chosen plate in to a draw
    pickedPlate = plate
    app.correctedPlate = []
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
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
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if (cx == app.playerX and cy == app.playerY):
            check = False  
    return check

def pickedUp(app):
        for i in range(len(app.foodCoords)):
            cx, cy, color, outline = app.foodCoords[i]
            if ifAlreadyHolding(app) == True:
                if (abs(app.playerX - cx) <= 25 and
                abs(app.playerY - cy) <= 25):
                    px = app.playerX
                    py = app.playerY
                    app.foodCoords[i] = (px, py, color, outline)
                    return

def moveLeft(app):
    app.playerX -= 20 
    if (app.playerX - app.playerR < 0):
        app.playerX = app.playerR
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX + 20 and cy == app.playerY:
            if app.holding == True:
                app.foodCoords[i] = (cx-20,cy,color,outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerX += 20
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX - 20 and cy == app.playerY:
            if app.holding == True and collision(app, cx, cy) != True:
                app.foodCoords[i] = (cx+20, cy, color, outline)

def moveRight(app):
    app.playerX += 20
    if (app.playerX + app.playerR > app.width):
        app.playerX = app.width - app.playerR
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX - 20 and cy == app.playerY:
            if app.holding == True:
                app.foodCoords[i] = (cx+20,cy,color, outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerX -= 20
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX + 20 and cy == app.playerY:
            if app.holding == True and collision(app, cx, cy) != True:
                app.foodCoords[i] = (cx-20, cy, color, outline)

def moveUp(app):
    app.playerY -= 20
    if (app.playerY - app.playerR < 0):
        app.playerY = app.playerR
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX and cy == app.playerY + 20:
            if app.holding == True:
                app.foodCoords[i] = (cx,cy-20,color, outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerY += 20
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX and cy == app.playerY - 20:
            if app.holding == True and collision(app, cx, cy) != True:
                app.foodCoords[i] = (cx, cy+20, color, outline)

def moveDown(app):
    app.playerY += 20
    if (app.playerY + app.playerR > app.height):
        app.playerY = app.height - app.playerR
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX and cy == app.playerY - 20:
            if app.holding == True:
                app.foodCoords[i] = (cx,cy+20,color, outline)
    if collision(app, app.playerX, app.playerY) != True:
        app.playerY -= 20
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        if cx == app.playerX and cy == app.playerY + 20:
            if app.holding == True and collision(app, cx, cy) != True:
                app.foodCoords[i] = (cx, cy-20, color, outline)


# def clearPlate(app):


def nearPlate(app):
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        x0, y0, x1, y1 = app.plateCoords[0]
        #328.0 <= 350 <= 372.0 and 47 + 25 >= 65)
        if (outline == "yellow" and ((cx <= x1 + 30)
        and (y1 + 20 >= cy)) and app.holding == False):
            app.assembledPlate += [(cx, cy, color, outline)]
            px = x1 - 20
            py = y1 - 20
            app.foodCoords[i] = (px, py, color, outline)
            
            
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
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        x0, y0, x1, y1 = app.trashCoords[0]
        if (((y0 <= cy <= y1) and (x0 - 20 <= cx) or
        (x0 <= cx <= x1) and (y0 - 10 <= cy)) 
        and app.holding == False):
            app.foodCoords[i] = (cx + 10**10, cy + 10**10,
                                "light grey", "lightgrey")

def nearOven(app):
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        x0, y0, x1, y1 = app.ovenCoords[0]
        if (color == "light yellow" and
        ((x0 <= cx <= x1) and (y0 - 20 <= cy)) 
        and app.holding == False):
            app.foodCoords[i] = (cx,cy,color, "yellow")
        
def nearStove(app):
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        x0, y0, x1, y1 = app.stoveTopCoords[0]
        if (color == "pink" and
        ((x0 <= cx <= x1) and (y0 - 20 <= cy)) 
        and app.holding == False):
            app.foodCoords[i] = (cx,cy,color, "yellow")

def nearChop(app):
    for i in range(len(app.foodCoords)):
        cx, cy, color, outline = app.foodCoords[i]
        x0, y0, x1, y1 = app.cuttingBoardCoords[0]
        if (color == "light green" and ((x0 <= cx <= x1) and (y0 + 20 >= cy))
        and app.holding == False):
            app.foodCoords[i] = (cx,cy,color, "yellow")

def clearPlate(app):
    copyL = copy.deepcopy(app.foodCoords)
    for i in range(len(copyL)):
        x0, y0, x1, y1 = app.plateCoords[0]
        cx, cy, color, outline = app.foodCoords[i]
        if (cx == (x1 - 20) and cy == (y1 - 20)):
            tx = cx + 10**10
            ty = cy + 10**10
            app.foodCoords[i] = (tx,ty,"light grey", "white")

# hw3.py name: E.j. Ezuma-Ngwu andrew id: ufe
def reverseList(L):
    return L[::-1]

def takeOffOne(app):
    copyL = (copy.deepcopy(app.foodCoords))
    rCopyL = reverseList(copyL)
    for i in range(len(copyL)):
        x0, y0, x1, y1 = app.plateCoords[0]
        cx, cy, color, outline = app.foodCoords[i]
        if (cx == (x1 - 20) and cy == (y1 - 20)):
            tx = cx + 10**10
            ty = cy + 10**10
            app.foodCoords[i] = (tx,ty,"light grey", "white")
            return
            
def keyPressed(app, event):
    if (event.key == "r"):
        initOvercooked(app)
    elif app.gameOver != True:
        #l for lettuce
        if (event.key == "v"):
            if nearVeggieFridge(app):
                randX = random.randint(((app.width/2) - 100), ((app.width/2) + 100))
                randY = random.randint(((app.height/2) + 50), ((app.height/2) + 60))
                app.foodCoords += [(randX, randY, "light green", "grey")]

        #m for meat
        if (event.key == "m"):
            if nearMeatFridge(app):
                randX = random.randint(((app.width/2) - 100), ((app.width/2) + 100))
                randY = random.randint(((app.height/2) + 50), ((app.height/2) + 60))
                app.foodCoords += [(randX, randY, "pink", "grey")]

        #d for dough
        if (event.key == "d"):
            if nearDoughBox(app):
                randX = random.randint(((app.width/2) - 100), ((app.width/2) + 100))
                randY = random.randint(((app.height/2) + 50), ((app.height/2) + 60))
                app.foodCoords += [(randX, randY, "light yellow", "grey")]

        if (event.key == "Space"):   
            for i in range(len(app.foodCoords)):
                cx, cy, color, outline = app.foodCoords[i]
                if (abs(app.playerX - cx) <= 30 and
                abs(app.playerY - cy) <= 30):
                    app.holding = not app.holding
                    if app.holding == True:
                        pickedUp(app)

        if (event.key == 'Left'):
            moveLeft(app)
            
        elif (event.key == 'Right'):
            moveRight(app)
        
        elif (event.key == 'Up'):
            moveUp(app)
            
        elif (event.key == 'Down'):
            moveDown(app)
        elif (event.key == 't'):
            takeOffOne(app)
        elif (event.key == 'Tab'):
            print(f"""your plate is {app.correctedPlate}
            you need {app.chosenPlate}""")
            if checkTicket(app, app.chosenPlate) == True:
                print("yay")
                clearPlate(app)
                app.correctedPlate = []
                app.customerColors.pop(0)
            else:
                app.score -= 1

def drawSpawnedIngredient(app, canvas):
    # startX = random.randint(((app.width/2) - 100), ((app.width/2) + 100))
    # startY = random.randint(((app.height/2) + 50), ((app.height/2) + 100))
    r = 15
    for i in range(len(app.foodCoords)):
        cx,cy,color,outline = app.foodCoords[i]
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, width = 3,
        outline = outline)
        # print(app.foodCoords)
#instead of directly drawing we append to an existing list
#use tuple in redraw all 
def drawCounterTops(app, canvas):
    for i in range(len(app.counterTopCoords)):
        x0,y0,x1,y1 = app.counterTopCoords[i]
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
        
def drawCuttingBoard(app, canvas):
    for i in range(len(app.cuttingBoardCoords)):
        x0,y0,x1,y1 = app.cuttingBoardCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "white", 
        outline = "light blue", width = 3)
        canvas.create_rectangle(x1 - 10, y0 - 5, x1 - 5, y1 + 5, 
        fill = "brown", outline = "light blue", width = 2)
        canvas.create_text(x0+25 ,y0 - 37, text='Cutting Board',
        font='Calibri 10 bold', fill='light grey')

def drawGameOver(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light grey")
    canvas.create_text(app.width/2, app.height/2 - 200, fill = "orange",
    font = "Calibri 35 bold", text = "Game Over!")
    if app.score >= 3:
        canvas.create_text(app.width/2, app.height/2, fill = "blue",
    font = "Calibri 20 bold", width = app.width/2 + 200,
    text = f"Your Score was: {app.score} Meaning You WON! Press r to Restart")
    else: 
        canvas.create_text(app.width/2, app.height/2, fill = "blue",
    font = "Calibri 20 bold", width = app.width/2 + 200,
    text = f"Your Score was: {app.score}, Meaning You Lost Unfortunately! Press r to Restart")

def drawPlate(app, canvas):
    for i in range(len(app.plateCoords)):
        x0, y0, x1, y1 = app.plateCoords[i]
        canvas.create_rectangle(x0-3,y0+3,x1-3,y1+3, fill="light grey", 
        width = 2, outline = "black")
        canvas.create_rectangle(x0,y0,x1,y1, fill="white", width = 2,
        outline = "black")
        canvas.create_text(x0 + 20, y0 -10, text='Plate',
        font='Calibri 10 bold', fill='black')
        canvas.create_text(x0 + 100, y0, 
        text="Bring the Processed Ingredients to the Plate in the Right Order.",
        font='Calibri 10 bold',
        fill='green', width = 75)
        canvas.create_text(x0, y0 + 100, 
        text="Press Tab to Check your Dish! You Will Get 1 Point if it's Correct or Lose a Point if it's Wrong.",
        font='Calibri 10 bold',
        fill='green', width = 90)
        canvas.create_text(x0 + 100, y0 + 80, 
        text="If You Need to Throw Away the Top-Most Ingredient, Press t!",
        font='Calibri 8 bold',
        fill='black', width = 100)

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
            #1rd customer
            canvas.create_rectangle(x0 + 110,y0 + 20, x0 + 130,y1 - 20, fill = app.customerColors[i],
            outline = "yellow", width = 3)

            canvas.create_oval(x0 + 110, y0, x0 + 130, y0 + 20, fill = app.skin)
            return

def drawTimer(app, canvas):
    for i in range(len(app.customerLineCoords)):
        x0, y0, x1, y1 = app.customerLineCoords[i]
        canvas.create_text(app.width - 50, 30, text= f'Time: {app.timer}',
        font='Calibri 15 bold', fill='black')

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light grey")
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
    canvas.create_text(app.width/2, app.height/10, 
    text="Use any Arrow Keys to Move and the SpaceBar to Pickup and Drop Your Ingredient.",
    font='Calibri 15 bold',
    fill='purple', width = 300)
    canvas.create_text(app.width/2, app.height/5, 
    text="Walk to a Fridge or Box to Spawn an Ingredient and Take it to the Right Place.",
    font='Calibri 15 bold',
    fill='blue', width = 300)
    canvas.create_oval(app.playerX-app.playerR, app.playerY-app.playerR,
                       app.playerX+app.playerR, app.playerY+app.playerR,
                       fill='cyan')
    drawSpawnedIngredient(app, canvas)
    drawTicket(app, canvas)
    
    if app.gameOver == True:
        print("56")
        drawGameOver(app, canvas)

    

runApp(width=600, height=600)