from pickle import load, UnpicklingError
from numpy import asarray
from numpy.random import randint, uniform

class Unpack():
    def __init__(self, simMode):
        self.simMode = simMode
        self.dataIn = []
        self.dataOut = Sensors()

    def getBlobs(self, data):
        depths = []
        xpos = []
        ypos = []
        widths = []
        for obj in data.objects:
            depths.append(obj.depth)
            widths.append(obj.width)
            xpos.append(obj.xpos)            
            ypos.append(obj.ypos)

        self.dataOut.xpos = asarray(xpos)
        self.dataOut.ypos = asarray(ypos)
        self.dataOut.widths = asarray(widths)
        self.dataOut.depths = asarray(depths)

    def getPos(self, data):
        self.dataOut.bikePosM = data.laneData.pob
        self.dataOut.targetPosM = data.laneData.lhs/4
        self.dataOut.bikePosM /= 1000000
        self.dataOut.targetPosM /= 1000000        
        self.dataOut.bikePosPx = data.laneData.pob_pixel
        self.dataOut.targetPosPx = data.laneData.lhs_pixel//4

    def getFrame(self, data):
        self.dataOut.frame = data.output_frame

    def translate(self, data):
        self.getBlobs(data)
        self.getPos(data)
        self.getFrame(data)
        # speed does not need to be translated
    
    def setup(self, pickleFilename = None):
        if self.simMode:
            self.setupSim(pickleFilename)
        else:
            self.setupAuto()

    # built for simMode     
    def unpickleFile(self, fileName):
        try:
            with open(fileName, 'rb') as pickleIn:
                return load(pickleIn)
        except UnpicklingError as e:
            print('An exception occured: ', e)

    def setupSim(self, pName):
        # TODO this might be alot of data to store constantly 
        self.pickleFilename = pName 
        self.dataIn = self.unpickleFile(pName)

    # built for autodrive 
    def unpickleObj(self):
        pass
           

    def setupAuto(self):
        pass 

class Sensors():
    def __init__(self):
        # these are np.arrays
        self.blobXpos = randint(0, size=0)
        self.blobYpos = randint(0, size=0)
        self.blobDepths = uniform(size=0)
        self.blobWidths = randint(0, size=0)
        self.frame = randint(0, size=0)
        # these are ints 
        self.bikePosPx = 0 
        self.targetPosPx = 0
        # these are floats 
        self.bikePosM = 0
        self.targetPosM = 0
        self.bikeSpeed = 0


if __name__ == "__main__":
    # intialization 
    simMode = 1
    pickleFilename = ''
    unpack = Unpack(simMode)
    unpack.setup(pickleFilename)
    # inside loop 
    for data in unpack.dataIn:
        unpack.translate(data)
        # call to autodrive(unpack.dataOut)
