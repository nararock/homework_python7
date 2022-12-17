from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.__color = "red"
            print(self.__color)
            sleep(7)
            self.__color = "yellow"
            print(self.__color)
            sleep(2)
            self.__color = "green"
            print(self.__color)
            sleep(5)


traffic1 = TrafficLight()
traffic1.running()
