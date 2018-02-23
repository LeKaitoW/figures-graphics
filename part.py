import body


class Part():
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

    def redraw(self, painter, *size):
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
