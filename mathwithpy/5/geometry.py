

from math import dist
from processing_py import *

def f541():
    t = 0
    app = App(600,600) 
    app.background(255)
    app.translate(app.width/2,app.height/2)
    app.rotate(radians(t))
    for i in range(12):
        app.rect(200,0,50,50)
        app.rotate(radians(360/12))

    t+=0.1
    app.redraw()


def f542():
    t = 0
    app = App(600,600) 
    while(True):
        app.background(255)
        app.translate(app.width/2,app.height/2)
        app.rotate(radians(t))
        for i in range(12):
            app.rect(200,0,50,50)
            app.rotate(radians((360/12)))

        t+=1
        app.redraw()
        #app.translate(300,300)
        # app.rect(200,0,50,50)
        # app.rotate(radians(360/12))
        # for i in range(12):
        #     app.pushMatrix()
        #     app.translate(200,0)
        #     app.rotate(radians(t))
        #     app.rect(0,0,50,50)
        #     app.popMatrix()
        #     app.rotate(radians(360/2))

        # t+=10
        # app.redraw()

    
def f543():
    t = 0
    app = App(600,600) 
    while(True):
        app.background(255)
        app.translate(app.width/2,app.height/2)
        #app.rotate(radians(t))
        for i in range(12):
            app.rectMode(CENTER)
            app.pushMatrix()
            app.translate(200,0)
            app.rotate(radians(t*5))
            app.rect(0,0,50,50)
            app.popMatrix()
            app.rotate(radians((360/12)))

        t+=1
        app.redraw()
        #app.translate(300,300)
        # app.rect(200,0,50,50)
        # app.rotate(radians(360/12))
        # for i in range(12):
        #     app.pushMatrix()
        #     app.translate(200,0)
        #     app.rotate(radians(t))
        #     app.rect(0,0,50,50)
        #     app.popMatrix()
        #     app.rotate(radians(360/2))

        # t+=10
        # app.redraw()

def f55():
        app = App(600,600) 
        app.rectMode(CENTER)
        app.colorMode(HSB)
        while(True):
            app.background(0)
            app.translate(20,20)
            for x in range(30):
                for y in range(30):
                    
                    d = dist((30*x,30*y),(app.mouseX,app.mouseY))
                    app.fill(0.5*d,255,255)
                    app.rect(20*x,30*y,25,25)


def main():
    f55()

if __name__ == "__main__":
    # execute only if run as a script
    main()