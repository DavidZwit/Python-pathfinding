#import tkinter
from tkinter import *
import Vector2
import circle
import time

oldTime = time.time()
currentTime = time.time()
'''the time the last frame took'''
deltaTime = 0
'''the total time the game is running'''
timePlaying = 0
'''the amound of loop cycles that have been done'''
loopCount = 1

shouldReset = False

def start() :
    ''' starts the whole program'''
    root = Tk()
    canvas = Canvas(root, width = 1200, height = 800)
    
    root.bind('<Motion>', motion)
    root.bind('<Button-1>', click)
    root.bind('<ButtonRelease-1>', mouseStop)

    canvas.pack()

    while True:
        global currentTime
        global oldTime
        global deltaTime
        global timePlaying
        
        currentTime = time.time()
        deltaTime = currentTime-oldTime
        timePlaying += deltaTime
        
        oldTime = currentTime

        global loopCount 

        if (timePlaying/loopCount > .03):
            loopCount += 1
            mainLoop(canvas, root)


def motion (event) :
    circle.Input(Vector2.new(event.x, event.y)) 

def click (event) :
    circle.Click() 

def mouseStop (event) :
    circle.StopClick()

def mainLoop(canvas, root):
    '''The main loop that does all the functions'''
    clear(canvas)

    global timePlaying
    global shouldReset
    if (int(timePlaying) % 7 == 0):
        
        if (shouldReset == True):
            circle.reset()


            print('\n', "[[[[[[[]]]]]]]", '\n' , "    reset", '\n', "[[[[[[[]]]]]]]", '\n')


        shouldReset = False
    else: 
        update()
        circle.drawPath(canvas)
        
        shouldReset = True

    draw(canvas)
    root.update()
def update():
    '''update all the objects'''
    for i in circle.obj:
        circle.obj[i].update()

    circle.Update()


def draw(canvas):
    '''draw all the objects'''
    #draw everything
    for i in circle.obj:
        circle.obj[i].draw(canvas)

def clear(canvas):
    '''clear the screen'''
    canvas.delete('all')

if __name__ == '__main__':
    start()  
