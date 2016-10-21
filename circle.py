import Vector2
import graphicalShapes
import collisions
import calculateBestDistance

from random import randint

#objects for saving the data
'''the objects that will be stored and drawed and updated and such'''
obj = {}
'''The paths the objects have done wich will be sorted'''
paths = {}
'''The best path wich will be used by the others'''
bestPath = []
'''The score the last winner had'''
lastWinnerScore = 0

draggingObj = 0

#Teakable variables


'''The frames skipped before the positions of the players are saved'''
frameSkipPositionSave = 5  

'''How much the circles will randomly move'''
randomFactor = 90  

'''The amound of players that will be participating'''  
amoundOfPlayers = 20 

#counters and such
'''The final target position that should be reached'''
targetPos = Vector2.new(1100, 400)
'''A counters that makes the path not update every frame'''
pathCounter = 0
'''Gives in wich frame we are each cicle'''
frameCounter = 0
'''The times the program has runed'''
cicleCounter = 0



def reset() :
    '''Reset the whole thing and save the best path'''
    global frameCounter
    print("frames done: ", frameCounter)
    frameCounter = 0

    global cicleCounter
    cicleCounter += 1

    for i in obj :
        if 'guy' in i :
            obj[i].followBehavour += 1

    global bestPath
    global amoundOfPlayers

    tempPath = calculateBestDistance.bestPath(paths, targetPos, cicleCounter, bestPath, True)
    obj[tempPath].followBehavour /= 4

    if not (tempPath is int): 
        bestPath = []

        #beste positiie werkt net!!!
            
        bestPath = paths[tempPath]

 
    for i in obj:
        obj[i].reset()


def drawPath(c) :
    '''Drawing last optimal path'''
    global bestPath
    global targetPos
    #Drawing the target position
    c.create_arc(targetPos.x-10, targetPos.y-10 ,targetPos.x+10, targetPos.y + 10, start=0, extent=359.99, fill='red')
    
    #print(frameCounter)
    #drawing the dot on the best position from last round
    try :
        currBestPath = bestPath[frameCounter]
        c.create_arc(currBestPath.x - 5, currBestPath.y - 5, currBestPath.x + 5, currBestPath.y +5, start=0, extent=359.99, fill='red')
    except : 
        pass

    for i in range (0, len(bestPath)-1): 
        #drawing a dot at each new line drawn  
        c.create_arc(int(bestPath[i].x)-1.5, int(bestPath[i].y)-1.5,int(bestPath[i].x)+1.5, int(bestPath[i].y) + 1.5, start=0, extent=359.99, fill='red')
        #drawing the last best path
        c.create_line(int(bestPath[i].x), int(bestPath[i].y), int(bestPath[i+1].x), int(bestPath[i+1].y), fill='black') 




#inputs
clicking = False
mousePos = Vector2.new()

def Input(pos) :
    global mousePos
    mousePos.x = pos.x
    mousePos.y = pos.y

def Click() :
    global clicking
    clicking = True

def StopClick() :
    global clicking
    clicking = False

#end inputs

stoppedInput = False
startInput = False
currentRectangle = 0
rectangleCount = 0

def Update():
    global frameCounter
    global pathCounter
    global targetPos

    global clicking
    global mousePos

    global stoppedInput
    global startInput

    global currentRectangle
    global rectangleCount 

    if (clicking) :
        stoppedInput = False
        #first time clicking
        if not (startInput) :
            startInput = True
            if (collisions.circleToPoint( mousePos, targetPos, 20 ) ) :
                targetPos = mousePos
            else : 
                obj['rect' + str(rectangleCount)] = graphicalShapes.rectangle(Vector2.new(mousePos.x, mousePos.y), Vector2.new())
                currentRectangle = obj['rect' + str(rectangleCount)]
                rectangleCount += 1

        if not (type(currentRectangle) is int ) : 
            currentRectangle.size = Vector2.new(
            mousePos.x - currentRectangle.position.x, 
            mousePos.y - currentRectangle.position.y) 

    #first time stopping with clicking
    elif not (stoppedInput) : 
        stoppedInput = True
        startInput = False
        currentRectangle = 0
        targetPos = Vector2.new(targetPos.x, targetPos.y)


    for i in obj:
        if ('rect' in i) :
            if (collisions.rectanglePoint(obj[i], mousePos)) : 
                #print('mouse in ', i)
                pass

    #calculating when to save the paths
    if (pathCounter >= frameSkipPositionSave):
        #every time the the path can be saved a frame is added
        frameCounter+=1
        print('adding frame ', frameCounter)
        pathCounter = 0
        

        ###check if a circle is colliding with a rectangle
    for i in obj :
        if ('rect' in i) :
            for x in obj :
                if ('guy' in x) :
                    if (collisions.rectanglePoint( obj[i], obj[x].position )) :
                        obj[x].shouldStop = True
                        pass

    pathCounter = pathCounter + 1
    

class path :
    '''create a object that will ceep track of what path you took'''
    def __init__(self, _startPos, _name):
        global paths
        self.name = _name
        self.startPos = Vector2.new(_startPos.x, _startPos.y)
        paths[self.name] = [_startPos]

    def addPos(self, pos) :
        '''Ad a position to the traveled path'''
        global paths
        
        #gets the array for this path and adds the new position
        paths[ self.name ].append( Vector2.new(pos.x, pos.y) )


    def newCycle(self):
        '''reset tha value's and start a new cicle'''
        global paths

        #reseting own position array
        paths[self.name] = []
        paths[self.name] = [self.startPos]
        


class searcher (graphicalShapes.arrow):
    '''The guy that will search for the position'''
    def __init__(self, _position, _radius, _color, _name, _doUpdate):
        self.velocity = Vector2.new()
        graphicalShapes.arrow.__init__(self, _position, _radius, _color)
        self.path = path(self.position, _name)
        self.doUpdate = _doUpdate
        self.name = _name
        self.target = Vector2.new(self.path.startPos.x, self.path.startPos.y)
        self.shouldStop = False
        '''How much the players listen to the best path ( the higher the less they will follow )'''
        self.followBehavour = 10

    def draw(self, c):
        '''draw the guy'''
        global pathCounter
        global frameSkipPositionSave

        super().draw(c)
        if (pathCounter >= frameSkipPositionSave) :
            c.create_line(self.position.x, self.position.y, self.target.x, self.target.y, fill='black')
        

    def update(self):
        '''update the guy'''
        global randomFactor

        global pathCounter
        global frameSkipPositionSave

        #if i should create a new position do that!
        if (pathCounter >= frameSkipPositionSave):
            if not (self.shouldStop) :
            
                #setting the random velocity
                self.velocity.rand(randomFactor, randomFactor)

                #if there is a 'best last round point' for this frame
                if (len(bestPath) -1 > frameCounter) :
                    currBestPath = bestPath[frameCounter]

                    #calculating the distance from the desired point divided by how much it unvluences it
                    velocityOffset = Vector2.new(
                        int((currBestPath.x - self.position.x) / self.followBehavour), 
                        int((currBestPath.y - self.position.y) / self.followBehavour)
                    )

                    #adding the little push towards the best position
                    self.target.x += velocityOffset.x
                    self.target.y += velocityOffset.y

                #aplying the velocity to the position
                self.target.x += self.velocity.x
                self.target.y += self.velocity.y

                #adding this step to the position array
            else : 
                self.target.x = 0
                self.target.y = 0

        self.path.addPos(self.target)
        self.position.x += (self.target.x - self.position.x)/20
        self.position.y += (self.target.y - self.position.y)/20
    
    def reset(self):
        '''reset it's value's and path'''
        #executing the reset function in the paths 
        self.path.newCycle()
        #setting position to start pos
        self.position.x = self.path.startPos.x
        self.position.y = self.path.startPos.y
        #reset targetPos
        self.target.x = self.position.x
        self.target.y = self.position.y
        #resetting velocity to 0
        self.velocity = Vector2.new()
        self.shouldStop = False



'''Creating the players'''
for i in range(amoundOfPlayers):
    obj["guy" + str(i)] = searcher(Vector2.new(80, 800/2), 10, 'green', 'guy' + str(i), True)