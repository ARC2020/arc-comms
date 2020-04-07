class ObjData():
    x = 0
    y = 0
    width = 0
    depth = 0

    def __init__(self, x, y, radius, depth):
        self.x = x
        self.y = y
        self.width = radius * 2
        self.depth = depth

    