class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class CheckMark:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __bool__(self):
        if self.a.x == self.b.x == self.c.x or self.a.y == self.b.y == self.c.y:
            return False
        if self.a.get_coords == self.b.get_coords:
            return False
        if self.a.get_coords == self.c.get_coords:
            return False
        if self.b.get_coords == self.c.get_coords:
            return False
        if (self.a.x - self.b.x == self.b.x - self.c.x) and (
            self.a.y - self.b.y == self.b.y - self.c.y
        ):
            return False
        return True

    def __eq__(self, other):
        if (
            self.a.x == other.a.x
            and self.a.y == other.a.y
            and self.b.x == other.b.x
            and self.b.y == other.b.y
            and self.c.x == other.c.x
            and self.c.y == other.c.y
        ) or (
            self.a.x == other.c.x
            and self.a.y == other.c.y
            and self.b.x == other.b.x
            and self.b.y == other.b.y
            and self.c.x == other.a.x
            and self.c.y == other.a.y
        ):
            return True
        return False

    def __str__(self):
        return "".join([self.a.name, self.b.name, self.c.name])
