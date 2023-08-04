class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
        self._size = [self._height, self._width]

    @property 
    def size(self):
        return self._size

    @property
    def area(self):
        return self._size[0]*self._size[1]

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._size = [self._height, self._width]

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._size = [self._height, self._width]


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
        self._size = [self._height, self._width]

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value
        self._size = [self._height, self._width]

# This function only works on Rectangle, does not work on other derived
def use_it(rc):
    rc.height = 10  # unpleasant side effect
    expected = int(rc.width * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
