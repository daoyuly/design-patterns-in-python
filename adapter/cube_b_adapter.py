from interface_cube_a import ICubeA
from cube_b import CubeB

class CubeBAdapter(ICubeA):

    def __init__(self):
        self.cube_b = CubeB()
        self.width = self.height = self.depth = 0

    def manufacture(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        success = self.cube_b.create(
            [0-width/2, 0-height/2, 0-depth/2],
            [0+width/2, 0+height/2, 0+depth/2]
        )
        return  success
