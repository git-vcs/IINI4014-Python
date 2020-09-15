import turtle as t
import time

def moveWithNoDrawing(posisiton):
    t.penup()
    t.goto(posisiton[0],posisiton[1])
    t.pendown()



def getNext(input):
    # input can reset the pointer to the array
    # if the input is -1 the methode returns the next possitions
    while True:
        print("input",input)
        if input == -1 and input <10:
            input=0
            yield input
            input += 1
        elif input>=10:
            input=0
            yield input
            input += 1
        else:
            yield input
            input+=1

    # return the current possition without incrementing








def main():
    test=getNext(-1)
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print("forandrer til 5")
    test=getNext(5)
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print("forandrer til 1")

    test=getNext(1)
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())
    print(test.__next__())



if __name__ == "__main__":
    # execute only if run as a script
    main()



