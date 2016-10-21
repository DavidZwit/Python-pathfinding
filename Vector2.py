from random import randint
import math

class new () :
    '''create a new vector2'''

    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, other):
        '''Add a vector to a vector'''
        self.x += other.x
        self.y += other.y

    def rand(self, randOffsetX, randOffsetY) :
        '''Set vector to a random vector'''
        self.x = randint(-randOffsetX, randOffsetX + int(randOffsetX/4) )
        self.y = randint(-randOffsetY, randOffsetY)

    def distance(self, target) :
        '''calculate distance between vectors'''
        return math.sqrt( (target.x - self.x)**2 + (target.y - self.y)**2 )

    def nonRootedDistance(self, target) :
        '''calculate unrooted distence between to vectors'''
        return (target.x - self.x)**2 + (target.y - self.y)**2

    def copy(self) :
        return new(self.x, self.y)

    def offset(self, other) :
        return new(self.x - other.x, self.y - other.y)
