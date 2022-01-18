from json.tool import main
from processing_py import *

xmin=-10
xmax=10

#range of y-values
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin
app = App(600,600) # create window: width, height

def setup():
    global xscl, yscl
    xscl=app.width / rangex
    yscl= -app.height / rangey


def grid(xscl, yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    app.strokeWeight(1)
    app.stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        app.line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin,ymax+1):
        app.line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    app.stroke(0) #black axes
    app.line(0,ymin*yscl,0,ymax*yscl)
    app.line(xmin*xscl,0, xmax*xscl,0)

def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def graphFunction():
    x = xmin
    while x <= xmax:
        app.fill(0)
        app.line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1# 精度


setup()
app.background(255) # set background:  red, green, blue
app.translate(app.width/2,app.height/2)
grid(xscl, yscl)
app.noFill()
app.strokeWeight(1) 
app.stroke(0) 

app.strokeWeight(2)
app.stroke(255,0,0) 

graphFunction()
app.redraw() # refresh the window


