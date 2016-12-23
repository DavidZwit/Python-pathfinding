
class arrow (object) :
    '''A graphical object to actually draw a object'''
    def __init__(self, _position, _radius, _color):
        self.radius = _radius
        self.color = _color
        self.position = _position

    def draw(self, canvas):
        '''the draw function wich draws the circle'''
        posOffset = self.radius/2
        canvas.create_arc(self.position.x - posOffset, self.position.y - posOffset, self.position.x + posOffset, self.position.y + posOffset,
        start=0, extent=359.99, fill=self.color)

class rectangle(object) :
    def __init__(self, _position, _size) :
        self.position = _position
        self.size = _size

    def draw(self, c) :

        c.create_rectangle(self.position.x, self.position.y, self.position.x + self.size.x, self.position.y + self.size.y, fill = 'grey')

    def update(self) :
        pass

    def reset(self) :
        pass
