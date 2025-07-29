class Point():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
 
    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"
 
    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)
 
    def get_x(self):
        return int(self.x)
 
    def get_y(self):
        return int(self.y)
 
    def get_coords(self):
        return (self.x, self.y)
 
    def __invert__(self):
        return Point(self.name, self.y, self.x)