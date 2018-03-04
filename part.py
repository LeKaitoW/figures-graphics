class Part(object):
    def __init__(self):
        self.up = None
        self.down = None
        self.window = None
        self.hollow = None
        self.elevation = 1

    def set_up(self, up):
        self.up = up

    def set_down(self, down):
        self.down = down

    def set_window(self, window):
        self.window = window

    def set_hollow(self, hollow):
        self.hollow = hollow

    def set_elevation(self, ratio):
        self.elevation = ratio

    def set_up_width(self, up_width):
        self.up.set_width(up_width)

    def set_down_width(self, down_width):
        self.down.set_width(down_width)

    def draw(self, painter, *size):
        if self.down and size[2] != 1:
            down_size = list(size[:-1])
            down_size.append(1 - size[2])
            self.down.redraw(painter, size[1] * 2 // 3 * size[2], *down_size)
        if self.up and size[2] != 0:
            self.up.redraw(painter, 0, *size)
        if self.window:
            self.window.redraw(painter, *size)
        if self.hollow:
            self.hollow.redraw(painter, *size)
