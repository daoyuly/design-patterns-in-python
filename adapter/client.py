import time
import random

from cube_b_adapter import CubeBAdapter
from cube_a import CubeA

total_cubes = 5
counter = 0

while counter < total_cubes:
    width = random.randint(1, 10)
    height = random.randint(1, 10)
    depth = random.randint(1, 10)

    cube = CubeA()
    success = cube.manufacture(width, height, depth)

    if success:
        print(
            f"Company A building Cube id:{id(cube)}, "
            f"{cube.width}x{cube.height}x{cube.depth}"
        )
        counter = counter + 1
    else:
        cube = CubeBAdapter()
        success = cube.manufacture(width, height, depth)
        if success:
            print(
                f"Company B building Cube id:{id(cube)}, "
                f"{cube.width}x{cube.height}x{cube.depth}"
            )
            counter = counter + 1
        else:
            print("Company B is busy, trying company A")

        time.sleep(1)

