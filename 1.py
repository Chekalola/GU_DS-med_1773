from time import sleep

class TrafficLight:
    colors = ("red", "yellow", 'green')
    pause = (7,2,10)

    def __init__(self):
        self.__color = "colors"


    def running(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(i)
                sleep(self.pause[self.colors.index(i)])

traffic_light = TrafficLight()
traffic_light.running()