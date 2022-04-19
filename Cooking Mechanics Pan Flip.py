
#Here are the cooking mechanics for the game

from cmu_112_graphics import *


#######################


def appStarted(app):
    
    app.c = 15


def redrawAll(app, canvas):
    bruh = app.c
    #draw pot, handle and fire circle underneath
    canvas.create_oval(150, 210, 450, 460, fill = "orange")
    #base pan
    canvas.create_oval(150, 205, 450, 405, fill = "grey" )
    #top pot
    canvas.create_oval(150, 205, 450, 360, fill = "brown" )
    #inside surface
    canvas.create_oval(155, 235, 445, 360, fill = "yellow" )
    #handle
    canvas.create_rectangle(450, 290, 560, 315, fill = "grey")
    #meat
    canvas.create_rectangle(250, 260, 350, 310, fill = "pink", 
    outline = "white", width = 6)




runApp(height = 600, width = 600)