class Road:

    def __init__(self,length, width):
        self.__length = length
        self.__width = width


    def asfalt_mass(self):
        result = self.__length * self.__width * 25 * 4
        return result

road_1 = Road(13, 17900)
print(road_1.asfalt_mass())
