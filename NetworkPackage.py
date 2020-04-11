class NetworkPackage():
    output_frame = None
    laneData = None
    objects = []

    def __init__(self, frame, laneData, objects):
        self.output_frame = frame
        self.laneData = laneData
        self.objects = objects

    def __str__(self):
        print("----------------")
        print("Lane LHS: ", self.laneData.lhs)
        print("Lane POB: ", self.laneData.pob)
        print("Lane LHS_pixel: ", self.laneData.lhs_pixel)
        print("Lane POB_pixel: ", self.laneData.pob_pixel)
        if (len(self.objects) > 0):
            print("Obj1 x: ", self.objects[0].x)
            print("Obj1 y: ", self.objects[0].y)
        print("----------------")
        return ""