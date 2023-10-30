from abc import ABCMeta,abstractmethod

class IHouseBuilder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        "building type"

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "wall_material"

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        "set_number_doors"

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        "set_number_windows"

class House:

    def __init__(self, building_type = "Apartment", wall_material = "Brick", doors = 0, windows = 0):
        self.building_type = building_type
        self.wall_material = wall_material
        self.doors = doors
        self.windows = windows

    def construct(self):
        "Returns a string describing the construction"
        return f"This is a {self.wall_material} " \
               f"{self.building_type} with {self.doors} " \
               f"door(s) and {self.windows} window(s)."


class HouseBuilder(IHouseBuilder):

    def __init__(self, house_designer):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self


    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self


class CastleDirector:

    def construct(self):
        return (HouseBuilder
                .set_wall_material("Sandstone")
                .set_number_windows(200)
                .set_number_doors(100)
                .set_building_type("Castle"))



class HouseBoatDirector:
    def construct(self):
        return (HouseBuilder
                .set_wall_material("Wood")
                .set_number_windows(10)
                .set_number_doors(6)
                .set_building_type("HouseBoat"))


class IglooDirector:
    def construct(self):
        return (HouseBuilder
                .set_wall_material("Ice")
                .set_number_windows(1)
                .set_number_doors(1)
                .set_building_type("Igloo"))


castle = CastleDirector().construct()
igloo = IglooDirector().construct()
houseboat = HouseBoatDirector().construct()