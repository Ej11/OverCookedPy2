from cmu_112_graphics import *









#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#moveDotWithArrowsAndBounds




def appStarted(app):
    app.playerX = (app.width/2)
    app.playerY = (app.height/2)
    app.playerR = 20
    app.holding = False
    #tuple of 2 x0,y0,x1,y1 coords
    app.counterTopCoords = [((app.width/2) -100, (app.height/2) + 50, 
            (app.width/2) + 100, (app.height/2) + 100), ((app.width/2) - 100, 
            (app.height/2) - 100, (app.width/2) + 100, (app.height/2) - 50) ]
            #[(300,400,200,400),(200,300,400,300)]
    app.serveTableCoords = [(0, (app.height/2) - 150, (app.width/2) - 200,
            (app.height/2) + 150 )]
    app.stoveTopCoords = [(app.width/2 -150, app.height - 50, 
    app.width/2 - 50, app.height - 5)]
    app.cabbageX = ((app.width/2) -50)
    app.cabbageY = ((app.height/2) + 75)
    app.cabbageR = 15
    # app.lettuceBorderColor = "green"
    # app.meatX = 
    # app.meatY =
    # app.meatR = 
    # app.meatBorderColor = "pink"

#checks to see if a collision occured
def collision(app, x, y):
    allObjs = app.counterTopCoords + app.serveTableCoords + app.stoveTopCoords
    for i in range(len(allObjs)):
        x0,y0,x1,y1 = allObjs[i]
        if (x0 <= x <= x1) and (y0 <= y <= y1):
            return False
    return True
    
def pickedUp(app):
    app.cabbageX = app.playerX
    app.cabbageY = app.playerY
    app.holding = not app.holding

def keyPressed(app, event):

    if (event.key == "Space"):
        # if ((app.playerX <= app.cabbageX + 40) or 
        # (app.playerX >= app.cabbageX - 40) and
        # ((app.playerY <= app.cabbageY + 40) or 
        # (app.playerY >= app.cabbageY - 40))):
        
        pickedUp(app)

    if (event.key == 'Left'):
        app.playerX -= 10
        if (app.playerX - app.playerR < 0):
            app.playerX = app.playerR
        if app.holding == True:
            app.cabbageX -= 10
        if collision(app, app.playerX, app.playerY) != True:
            app.playerX += 10
        if app.holding == True and collision(app, app.cabbageX, app.cabbageY) != True:
            app.cabbageX += 10
        
    elif (event.key == 'Right'):
        app.playerX += 10
        if (app.playerX + app.playerR > app.width):
            app.playerX = app.width - app.playerR
        if app.holding == True:
            app.cabbageX += 10
        if collision(app, app.playerX, app.playerY) != True:
            app.playerX -= 10
        if app.holding == True and collision(app, app.cabbageX, app.cabbageY) != True:
            app.cabbageX -= 10
    
    elif (event.key == 'Up'):
        app.playerY -= 10
        if (app.playerY - app.playerR < 0):
            app.playerY = app.playerR
        if app.holding == True:
            app.cabbageY -= 10
        if collision(app, app.playerX, app.playerY) != True:
            app.playerY += 10
        if app.holding == True and collision(app, app.cabbageX, app.cabbageY) != True:
            app.cabbageY += 10
        
    elif (event.key == 'Down'):
        app.playerY += 10
        if (app.playerY + app.playerR > app.height):
            app.playerY = app.height - app.playerR
        if app.holding == True:
            app.cabbageY += 10
        if collision(app, app.playerX, app.playerY) != True:
            app.playerY -= 10
        if app.holding == True and collision(app, app.cabbageX, app.cabbageY) != True:
            app.cabbageY -= 10


def drawCounterTops(app, canvas):
    for i in range(len(app.counterTopCoords)):
        x0,y0,x1,y1 = app.counterTopCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "brown", outline = "grey",
         width = 4)
def drawServeTable(app, canvas):
    for i in range(len(app.serveTableCoords)):
        x0,y0,x1,y1 = app.serveTableCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 3)
        canvas.create_text(x0 + 25 ,y0 + 150, text='Serve Table', angle = 90, 
                font='Calibri 15 bold', fill='white')
def drawStoveTop(app,canvas):
    for i in range(len(app.stoveTopCoords)):
        x0,y0,x1,y1 = app.stoveTopCoords[i]
        canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black",
        width = 2)
        canvas.create_oval(x0 + 5, y0 + 5, x0 + 45, y1 - 5, fill = "orange",
        outline = "yellow", width = "2")
        canvas.create_oval(x0 + 55, y0 + 5, x1 - 5, y1 - 5, fill = "orange",
        outline = "yellow", width = "2")
        canvas.create_text(x0+10 ,y0+10, text='Stove', font='Calibri 10 bold',
         fill='white')

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light yellow")
    drawCounterTops(app, canvas)
    drawServeTable(app, canvas)
    drawStoveTop(app,canvas)
    canvas.create_text(app.width/2, app.height/10, 
    text="Use Arrow Keys to Move and the SpaceBar to Pickup and Drop Your Ingredient", font='Calibri 20 bold',
    fill='purple', width = 250)
    canvas.create_oval(app.playerX-app.playerR, app.playerY-app.playerR,
                       app.playerX+app.playerR, app.playerY+app.playerR,
                       fill='orange')
    
    canvas.create_oval(app.cabbageX-app.cabbageR, app.cabbageY-app.cabbageR,
                       app.cabbageX+app.cabbageR, app.cabbageY+app.cabbageR,
                       fill='light green')
  


runApp(width=500, height=500)