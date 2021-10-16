class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула {direction}!')

    def show_speed(self):
        print(f'скорость автомобиля = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar(90, 'черный', 'BMW')
sport = SportCar(220, 'красный', 'Porsche')
work = WorkCar(50, 'желтый', 'Caterpillar')
police = PoliceCar(70, 'белый', 'Kia')
town.show_speed()
work.show_speed()
sport.turn('Направо')
print(sport.color)
print(sport.name)
print(police.is_police)
