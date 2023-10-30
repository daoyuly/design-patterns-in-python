import  time
from interface_cube_a import ICubeA

class CubeA(ICubeA):

    last_time = int(time.time())

    def __init__(self):
        self.width = self.height = self.depth = 0
    def manufacture(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        now = int(time.time())
        if now > int(CubeA.last_time + 1):
            CubeA.last_time = now
            return True
        return False

