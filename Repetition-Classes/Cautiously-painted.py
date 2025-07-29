class Point:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_coords(self) -> tuple:
        return (self.x, self.y)

    def __str__(self) -> str:
        return f"{self.name}({self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name: str, x: int, y: int, color: tuple = (0, 0, 0)):
        super().__init__(name, x, y)
        self.color = color

    def get_color(self) -> tuple:
        return self.color

    def __invert__(self):
        new_x, new_y = self.y, self.x
        r, g, b = self.color
        inverted_color = (255 - r, 255 - g, 255 - b)
        return ColoredPoint(self.name, new_x, new_y, inverted_color)
