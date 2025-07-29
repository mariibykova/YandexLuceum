class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
 
    def get_x(self):
        return int(self.x)
 
    def get_y(self):
        return int(self.y)
 
    def get_coords(self):
        return '({}, {})'.format(self.x, self.y)
 
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        if self.name == other.name and self.x == other.x and self.y == other.y:
            return True
        return False
 
    def __gt__(self, other):
        if self.name > other.name:
            return True
        elif self.x > other.x and self.name == other.name:
            return True
        elif self.y > other.y and self.x == other.x and self.name == other.name:
            return True
        else:
            return False
 
    def __lt__(self, other):
        if self.name < other.name:
            return True
        elif self.x < other.x and self.name == other.name:
            return True
        elif self.y < other.y and self.x == other.x and self.name == other.name:
            return True
        else:
            return False
 
    def __ge__(self, other):
        if self.name > other.name:
            return True
        elif self.x > other.x and self.name == other.name:
            return True
        elif self.y >= other.y and self.name == other.name and self.x == other.x:
            return True
        else:
            return False
 
    def __le__(self, other):
        if self.name < other.name:
            return True
        elif self.x < other.x and self.name == other.name:
            return True
        elif self.y <= other.y and self.x == other.x and self.name == other.name:
            return True
        else:
            return False
 
    def __hash__(self):
        return hash(self.name)
 
    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)
 
    def __repr__(self):
        return "Point('{}', {}, {})".format(self.name, self.x, self.y)
 
    def __invert__(self):
        return Point(self.name, self.y, self.x)