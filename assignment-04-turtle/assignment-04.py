import turtle as t  # defining t as synonymous with turtle
t.color('grey', 'yellow')
t.speed(0)
t.bgcolor("black")
pointArray=[] # stores positions to the points


# Generates a Circle and puts all the point values into pointArray
def makeCircle(rdius,numberOfDots,numbers=False,dots=False):
    pointArray.clear()
    i=0
    stepLentgh=365/numberOfDots #Determining the length between the dots
    while i < 360:
        t.circle(rdius,stepLentgh)
        if dots:
            t.dot(5,"green") # makes a dot

        if numbers:
            t.write(len(pointArray)) # Displays a number next to the point
        i+=stepLentgh
        pointArray.append(t.pos())



def drwaLine(position): #the method expect x, y-coordinates in the form [x,y]
    t.pendown()
    t.goto(position)






#method of moving the turtle without drawing at the same time
# posiston is [x,y] from origo
def moveWithNoDrawing(posisiton):
    if posisiton != -1:
        t.penup()
        t.goto(posisiton)
        t.pendown()



#Generating the timetables
def generateTimeTables(multiplier=2):
    list = getNext(-1,len(pointArray))
    currentDot = list.__next__() # fetching position to the current point
    moveWithNoDrawing(pointArray[currentDot])  # moving to the first point
    for everypoint in range(0,len(pointArray)):  # for every point in the array do the following
        currentDot = list.__next__()  # fetching the next value
        moveWithNoDrawing(pointArray[currentDot])  # moving to the dot we are going to start drawing from

        #finding the destination dot
        newPosisiton=0
        for b in range(0,multiplier-1):
            for i in range(0,currentDot):
                newPosisiton = list.__next__()
        drwaLine(pointArray[newPosisiton])  # moving to destination
        currentDot += 1
        list = getNext(currentDot,len(pointArray))  # resetting the list to the next point we are going to draw from



def getNext(input,maxSize):
    #  this is a method with generators that tries to use an array as an linked list
    #  this means that getNext return a number that is incremented with one every time until it hits the array limit, then it wraps around
    #  input can reset the pointer to the array to any given place in the array
    #  if the input is -1 the method returns the next positions
    while True:
        if input == -1 and input < maxSize:
            input = 0  #  resetting the value
            yield input
            input += 1
        elif input >= maxSize:
            input=0
            yield input
            input += 1
        else:
            yield input
            input += 1





def main():
    moveWithNoDrawing([0,-250])  # Moving turtle to accommodate lager circles
    circleSize=350
    numberOfDots=350
    #                               numbers,dots
    makeCircle(circleSize,numberOfDots,False,False)  # set True to false if you do't need numbers or dots
    generateTimeTables(350) # input the multiplier






if __name__ == "__main__":
    # execute only if run as a script
    main()
    t.done()  # preventing the from program closing
