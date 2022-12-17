class Road:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def calculate_asphalt(self):
        depth = 5
        density_asphalt = 2500  # плотность асфальта в кг/м^3
        weight = self.__width * self.__length * depth // 100 * density_asphalt
        return weight  # масса в кг


road = Road(20, 5000)
print(road.calculate_asphalt())
