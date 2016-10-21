import math

def circleToCircle(c1Pos, c1Radius, c2Pos, c2Radius) :

    if ( math.sqrt( (c2Pos.x - c1Pos.x)**2 + (c2Pos.y - c1Pos.y)**2 ) < c1Radius + c2Radius ) :
        return True
    else : return False

def circleToPoint(point, cPos, cRadius) :
    if (math.sqrt( (point.x - cPos.x)**2 + (point.y - cPos.y)**2 ) < cRadius) : 
        return True
    else : return False

def rectanglePoint(rect, point) :
        
    return ((point.x >= rect.position.x and point.x <= rect.position.x + rect.size.x) and
            (point.y >= rect.position.y and point.y <= rect.position.y + rect.size.y))