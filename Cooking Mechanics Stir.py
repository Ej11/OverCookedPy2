
#Here are the cooking mechanics for the game

from cmu_112_graphics import *


#######################
#

def appStarted(app):
    
    app.spoonPosX = 320
    app.spoonPosY = 70

def mouseDragged(app, event):
    app.spoonPosX = event.x
    app.spoonPosY = event.y


def redrawAll(app, canvas):
    #draw pot, handle and fire circle underneath
    #background
    canvas.create_rectangle(0, 0, 600, 600, fill = "light yellow")
    #fire
    canvas.create_oval(170, 190, 430, 450, fill = "orange")
    #bottom
    canvas.create_oval(200, 265, 400, 415, fill = "grey", outline = "grey" )
    #base
    canvas.create_rectangle(200, 150, 400, 350, fill = "grey", outline = "grey")
    #top pot
    canvas.create_oval(200, 100, 400, 200, fill = "grey" )
    #food
    canvas.create_oval(200, 125, 400, 200, fill = "yellow" )
    #spoon
    canvas.create_rectangle(app.spoonPosX, app.spoonPosY, 
    app.spoonPosX + 20, app.spoonPosY + 100, fill = "brown")
    
    

runApp(height = 600, width = 600)

# canvas.create_oval(170, 190, 430, 450, fill = "orange")
# #bottom
# canvas.create_oval(200, 250, 400, 400, fill = "grey" )
# #base
# canvas.create_rectangle(200, 150, 400, 350, fill = "grey", outline = "grey")
# #top pot
# canvas.create_oval(200, 100, 400, 200, fill = "yellow" )
# #spoon
# canvas.create_rectangle(320, 70, 330, 170, fill = "brown")