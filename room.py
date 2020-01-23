class Room:
    def __init__(self, coords):
        self.x1, self.y1 = coords
        # self.width = 32
        # self.height = 25
        self.width = 5
        self.height = 5
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height

    def __str__(self):
        output = f'x1,x2: ({self.x1}, {self.x2})\n'
        output += f'y1, y2: ({self.y1}, {self.y2})'
        return output

    @property
    def center(self):
        center_x = (self.x1 + self.x2)/2
        center_y = (self.y1 + self.y2)/2
        return (center_x, center_y)

    def intersect(self, other):
        objects_intersect = ( self.x1 <= other.x2 and
                              self.x2 >= other.x1 and
                              self.y1 <= other.y2 and
                              self.y2 >= other.y1 )
        return objects_intersect

