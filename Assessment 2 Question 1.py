import turtle
import random
polygon = turtle.Turtle()

sideCount = 6
sideLength = 80.0
angle = 360.0 / sideCount
startX = -560
startY = 560

downStep = 138

beeWindow = turtle.Screen()
beeWindow.setup(1200, 1050)
beeWindow.bgcolor("gold")

polygon.pensize(3)


#below are the functions used to draw the hex grid
#these are done as callable functions to be made resusable to easily construc the hex grid with reduced ammount of code

def upPoly(move, turn): #this function draws the top half of a polygon
    #a simple sequence of steps to draw half of an equal hexagon
    polygon.left(turn)
    polygon.forward(move)
    polygon.right(turn)
    polygon.forward(move)
    polygon.right(turn)
    polygon.forward(move)
    polygon.left(turn)

def spacer(move, turn): #this function spaces the polygons evenly
    #simply spaces the hexagons and draws a connected line
    polygon.forward(move)
    
def downPoly(move, turn): #this function draws the bottom half of the polygon
    #a simple sequence of steps to draw half of an equal hexagon
    polygon.right(turn)
    polygon.forward(move)
    polygon.left(turn)
    polygon.forward(move)
    polygon.left(turn)
    polygon.forward(move)
    polygon.right(turn)

def topHex(length): #this function combines the spacing in the hex function to construc the top half of the grid line
    for i in range(length): #draws the row
        upPoly(sideLength, angle)
        spacer(sideLength, angle)
    upPoly(sideLength, angle) #adds an extra hex half at the end to there is no spare spacer

def bottomHex(length): #this function combines the spacing in the hex function to construc the bottom half of the grid line
    for i in range(length): #draws the row
        downPoly(sideLength, angle)
        spacer(sideLength, angle)
    downPoly(sideLength, angle) #adds an extra hex half at the end to there is no spare spacer

def startPos(x, y): #this function sets the starting position for the hex1 grid
    polygon.penup()
    polygon.goto(x, y)
    polygon.pendown()

def drawHex(rows, offset): #this function combines the top and bottom hex functions into a fully formed grid
    rowCount = 0
    moveMod = offset*rowCount #moves the row down by the offset value for every row that is completed
    polygon.pencolor("orange")
    for i in range(rows): #draws number of rows per the desired value
        rowCount = rowCount + 1
        startPos(startX, startY-(offset*rowCount)) #sets starting pos and uses the modified value
        topHex(4) #draws the top hex set
        startPos(startX, startY-(offset*rowCount)) #resets starting pos using modified value
        bottomHex(4) #draws bottom hex set

def wingOval(r): #this function draws the oval for the bee wing
    polygon.fillcolor("white") #sets the colour of the wing fill
    polygon.begin_fill()
    for loop in range(2): #this loop draws a circle in quarters
        polygon.circle(r,90) # first quater with an unmodified radius and a limited degrees
        polygon.circle(r/6,90) #second quater with modified radius and limited degrees
    polygon.end_fill()

def drawBee(beePosX, beePosY, beeHeading): #this function combines some simple drawing with the wing function to draw a bee

    wingsize = 65
    r = 10
    headR = 20
    thoraxR = 10
    n = 4
    polygon.penup()
    polygon.goto(beePosX, beePosY)
    polygon.right(beeHeading)
    polygon.pencolor("black")
    polygon.pendown()
    polygon.right(15)
    polygon.forward(60)
    polygon.backward(60)
    polygon.left(30)
    polygon.forward(60)
    polygon.backward(60)
    polygon.right(100)
    polygon.fillcolor("yellow")
    polygon.begin_fill()
    polygon.circle(headR)
    polygon.end_fill()
    polygon.right(90)
    polygon.forward(100)
    polygon.backward(100)
    polygon.left(90)
    polygon.right(180)
    polygon.begin_fill()
    for i in range(1, n+1, 1):
        polygon.circle(thoraxR*i)
    polygon.end_fill()
    polygon.left(90)
    wingOval(wingsize)
    wingOval(-wingsize)

def drawEverything(bees): #this function combines the other functions with some random co-ordinates to draw the final image
    drawHex(7, downStep)
    for i in range(bees):
        beeX = random.randint(-500, 500)
        beeY = random.randint(-500, 500)
        beeFacing = random.randint(0,360)
        drawBee(beeX, beeY, beeFacing)

drawEverything(8)

turtle.done()