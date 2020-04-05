class NetworkPackage():
    laneData = None
    objects = []

    def __init__(self, laneData, objects):
        self.laneData = laneData
        self.objects = objects

    def __str__(self):
        print("----------------")
        print("Lane LHS: ", self.laneData.lhs)
        print("Lane POB: ", self.laneData.pob)
        if (len(self.objects) > 0):
            print("Obj1 x: ", self.objects[0].x)
            print("Obj1 y: ", self.objects[0].y)
        print("----------------")