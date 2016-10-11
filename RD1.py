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

def anyShape(y):
    penDown()
    for x in range (0,y):
        forward(2,1.5)
        turnBy(360/y)
    penUp()

sideNum = raw_input("How many sides would you like?")   
sideNum = int(sideNum)
anyShape(sideNum)
    