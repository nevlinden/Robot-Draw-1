from Myro import *
init ("sim")
def squareDraw():
    penDown()
    for x in range (0,4):
        forward(2,2)
        turnBy(90)
    penUp()
    
def triangleDraw():
    penDown()
    for x in range (0,3):
        forward (2,2)
        turnBy(120)
    penUp()

def someShapes():        
    squareDraw()
    turnBy(90)
    backward(1,2)
    triangleDraw()

someShapes()