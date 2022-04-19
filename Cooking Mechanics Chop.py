
#Here are the cooking mechanics for the game

from cmu_112_graphics import *


#######################


#add main objects into helper functions
def appStarted(app):

    app.c = 15


def redrawAll(app, canvas):
    b = app.c
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    #board
    canvas.create_rectangle(100, 200, 500, 400, fill = "cyan",
    outline = "green", width = 14 )
    #handle 
    canvas.create_rectangle(430, 250, 470, 350, fill = "light blue",
    outline = "green", width = 10 )
    #meat
    canvas.create_rectangle(150, 310, 400, 330, fill = "light green", 
    outline = "green", width = 3)
    #blade
    canvas.create_rectangle(250, 120, 350, 160, fill = "grey", outline = 
    "black", width = 3)
    #handle
    canvas.create_rectangle(352, 130, 400, 150, fill = "brown", outline = "black", width = 2)

runApp(height = 600, width = 600)