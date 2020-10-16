import random
import tkinter


class Dice:
    currentdicevaliue=-1
    dicecollorvaliue="blue"
    dicesize = 100
    dotcolor ="black"

    # Create a die whose position (x-y coordinates of one on the corners) and size is provided by the user.
    # Default constructor
    def __init__(self,xCoordinate,yCoordinate,size):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.dicesize=size

    # Access the position and size of the dice.
    def getposition(self):
        return [self.xCoordinate, self.yCoordinate]
        
    def getdicesize(self):
        return self.dicesize

    # Roll the dice.
    def rolldice(self):
        # generates a random value between 1 and 6
        self.currentdicevaliue = random.randrange(1, 7)

    # Access the value of the face shown on top of the dice.
    def getdicevaliue(self):
        return self.currentdicevaliue

    #Set the colour used to draw the dice and the colour of the dots (default colours are white and black).
    def setdicecolor(self, color):
        self.dicecollorvaliue=color

    def setdotcolor(self, color):
        self.dotcolor = color

    # Draw the die on a canvas.
    def draw(self, canvas):
        dotsize = self.dicesize*0.15
        padding = self.dicesize*0.1
        x0 = self.xCoordinate
        y0 = self.yCoordinate
        x1 = self.xCoordinate + self.dicesize
        y1 = self.yCoordinate + self.dicesize

        # Drawing the dice outline
        canvas.create_rectangle([x0,y0,x1,y1],fill=self.dicecollorvaliue)
        print("Printing dice:",self.getdicevaliue())
        if self.getdicevaliue() == 1:
            # middle dot
            canvas.create_rectangle([x0+(self.dicesize*0.5)-dotsize,y0+(self.dicesize*0.5)-dotsize,x0+(self.dicesize*0.5)+dotsize,y0+(self.dicesize*0.5)+dotsize],fill=self.dotcolor)

        if self.getdicevaliue() == 2:
            # upper lef dot
            canvas.create_rectangle([self.xCoordinate+padding,self.yCoordinate+padding,self.xCoordinate+dotsize+padding,self.yCoordinate+dotsize+padding],fill=self.dotcolor)
            # lower right dot
            canvas.create_rectangle([x1-padding, y1-padding, x1-dotsize-padding, y1-dotsize-padding], fill=self.dotcolor)

        if self.getdicevaliue() == 3:
            # middle dot
            canvas.create_rectangle([x0+(self.dicesize*0.5)-dotsize+padding*0.25, y0+(self.dicesize*0.5)-dotsize+padding*0.25, x0+(self.dicesize*0.5)+dotsize-padding*0.25, y0+(self.dicesize*0.5)+dotsize-padding*0.25],fill=self.dotcolor)
            # upper lef dot
            canvas.create_rectangle([self.xCoordinate+padding, self.yCoordinate+padding, self.xCoordinate+dotsize+padding, self.yCoordinate+dotsize+padding], fill=self.dotcolor)
            # lower right dot
            canvas.create_rectangle([x1-padding, y1-padding, x1-dotsize-padding, y1-dotsize-padding], fill=self.dotcolor)

        if self.getdicevaliue() == 4:
            # upper lef dot
            canvas.create_rectangle([self.xCoordinate+padding,self.yCoordinate+padding,self.xCoordinate+dotsize+padding,self.yCoordinate+dotsize+padding],fill=self.dotcolor)
            # lower right dot
            canvas.create_rectangle([x1-padding, y1-padding, x1-dotsize-padding, y1-dotsize-padding], fill=self.dotcolor)
            # lower left dot
            canvas.create_rectangle([self.xCoordinate+padding , y1-padding, self.xCoordinate+dotsize+padding, y1-dotsize-padding], fill=self.dotcolor)
            # upper right dot
            canvas.create_rectangle([x1-padding-dotsize , y0+padding+dotsize, x1-padding, y0+padding], fill=self.dotcolor)

        if self.getdicevaliue() == 5:
            # middle dot
            canvas.create_rectangle([x0+(self.dicesize*0.5)-dotsize+padding*0.25,y0+(self.dicesize*0.5)-dotsize+padding*0.25,x0+(self.dicesize*0.5)+dotsize-padding*0.25,y0+(self.dicesize*0.5)+dotsize-padding*0.25],fill=self.dotcolor)
            # upper lef dot
            canvas.create_rectangle([self.xCoordinate+padding,self.yCoordinate+padding,self.xCoordinate+dotsize+padding,self.yCoordinate+dotsize+padding],fill=self.dotcolor)
            # lower right dot
            canvas.create_rectangle([x1-padding, y1-padding, x1-dotsize-padding, y1-dotsize-padding], fill=self.dotcolor)
            # lower left dot
            canvas.create_rectangle([self.xCoordinate+padding , y1-padding, self.xCoordinate+dotsize+padding, y1-dotsize-padding], fill=self.dotcolor)
            # upper right dot
            canvas.create_rectangle([x1-padding-dotsize , y0+padding+dotsize, x1-padding, y0+padding], fill=self.dotcolor)

        if self.getdicevaliue() == 6:
            canvas.create_rectangle([self.xCoordinate+padding,self.yCoordinate+padding,self.xCoordinate+dotsize+padding,self.yCoordinate+dotsize+padding],fill=self.dotcolor)
            # lower right dot
            canvas.create_rectangle([x1-padding, y1-padding, x1-dotsize-padding, y1-dotsize-padding], fill=self.dotcolor)
            # lower left dot
            canvas.create_rectangle([self.xCoordinate+padding , y1-padding, self.xCoordinate+dotsize+padding, y1-dotsize-padding], fill=self.dotcolor)
            # upper right dot
            canvas.create_rectangle([x1-padding-dotsize , y0+padding+dotsize, x1-padding, y0+padding], fill=self.dotcolor)
            # left middle
            canvas.create_rectangle([x0+padding,y1-self.dicesize*0.5-dotsize+(padding*0.5),x0+dotsize+padding,y1-self.dicesize*0.5+(padding*0.5)],fill=self.dotcolor)
            # right middle
            canvas.create_rectangle([x1-padding,y1-self.dicesize*0.5-dotsize+(padding*0.5),x1-dotsize-padding,y1-self.dicesize*0.5+(padding*0.5)],fill=self.dotcolor)

    # debug method for printing all values in the class
    def tostring(self):
        print("x-Coordinate:",self.xCoordinate,"y-Coordinate:",self.yCoordinate)
        print("Dice size:",self.size)
        print("Color:",self.dicecollorvaliue)
        print("Dice Valiue:",self.currentdicevaliue)
        print("Dice Color",self.dicecollorvaliue)
        print("Dice dot",self.dotcolor)


# Setting-up the window and defining resolution and backgrounder
# Global variables
root = tkinter.Tk()
root.title("Assigment-08-dice")
root.geometry("800x400")
canvas = tkinter.Canvas(root, width=1600, height=800, bg="blue")
dice = Dice(120,157,150)


# event is called every time someone clinks inside the window
def click(event):
    global root
    global canvas
    global dice
    print("Click")
    dice.rolldice()
    dice.draw(canvas)


def main():
    global root
    global canvas
    global dice
    dice.setdicecolor("white")
    dice.setdotcolor("yellow")
    # Binding method to the canvas to be called on a click event
    canvas.bind("<Button-1>",click)
    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()





