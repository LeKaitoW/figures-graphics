from PyQt5.QtCore import *
from PyQt5.QtGui import *

# size - width, height, evaluation, corners


class Body(object):
    def __init__(self, *args):
        self.width = args[0]

    def redraw(self, painter, start, *size):
        print("here")

    def set_width(self, width):
        self.width = width


class Cone(Body):
    def __init__(self, *args):
        self.width = args[0]

    def redraw(self, painter, start, *size):
        painter.drawLine(size[0] // 2, start, size[0] // 2 - self.width // 2, start + size[1] * size[2] * 2 // 3)
        painter.drawLine(size[0] // 2, start, size[0] // 2 + self.width // 2, start + size[1] * size[2] * 2 // 3)
        painter.drawLine(size[0] // 2 - self.width // 2, start + size[1] * size[2] * 2 // 3,
                         size[0] // 2 + self.width // 2,
                         start + size[1] * size[2] * 2 // 3)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(QPoint(size[0] // 2, size[1] * 5 // 6), self.width // 2, self.width // 2)


class Cylinder(Body):
    def __init__(self, *args):
        super(Body, self).__init__()
        self.width = args[0]

    def redraw(self, painter, start, *size):
        painter.drawRect(size[0] // 2 - self.width // 2, start, self.width // 2 * 2, size[1] * size[2] * 2 // 3)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(QPoint(size[0] // 2, size[1] * 5 // 6), self.width // 2, self.width // 2)


class Sphere(Body):
    def __init__(self, *args):
        super(Body, self).__init__()
        self.width = args[0]

    def redraw(self, painter, start, *size):
        painter.drawEllipse(QPoint(size[0] // 2, start + size[1] * size[2] * 2 // 3 // 2), self.width//2, self.width//2)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(QPoint(size[0] // 2, size[1] * 5 // 6), self.width//2, self.width//2)


class Pyramid(Body):
    def __init__(self, *args):
        super(Body, self).__init__()


class TriangularPyramid(Pyramid):
    def __init__(self, *args):
        super(Pyramid, self).__init__()

    def redraw(self, painter, start, *size):
        pass


class QuadrangularPyramid(Pyramid):
    def __init__(self, *args):
        super(Pyramid, self).__init__()

    def redraw(self, painter, start, *size):
        pass


class PentagonalPyramid(Pyramid):
    def __init__(self, *args):
        super(Pyramid, self).__init__()

    def redraw(self, painter, start, *size):
        pass


class HexagonalPyramid(Pyramid):
    def __init__(self, *args):
        super(Pyramid, self).__init__()

    def redraw(self, painter, start, *size):
        pass

class Prism(Body):
    def __init__(self, *args):
        super(Body, self).__init__()

    def redraw(self, painter, *size):
        corners = size[3]


class TriangularPrism(Prism):
    def __init__(self, *args):
        super(Prism, self).__init__()

    def redraw(self, painter, *size):
        pass


class QuadrangularPrism(Prism):
    def __init__(self, *args):
        super(Prism, self).__init__()

    def redraw(self, painter, *size):
        pass


class PentagonalPrism(Prism):
    def __init__(self, *args):
        super(Prism, self).__init__()

    def redraw(self, painter, *size):
        pass


class HexagonalPrism(Prism):
    def __init__(self, *args):
        super(Prism, self).__init__()

    def redraw(self, painter, *size):
        pass