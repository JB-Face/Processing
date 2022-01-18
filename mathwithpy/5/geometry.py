
from fnmatch import translate
from math import radians
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




    

def main():
    f541()

if __name__ == "__main__":
    # execute only if run as a script
    main()