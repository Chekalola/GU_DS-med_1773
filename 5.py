class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print(f'Рисунок ручкой {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Рисунок карандашом {self.title}')

class Handle(Stationary):
    def draw(self):
        print(f'Рисунок маркером {self.title}')

pencil = Pencil('Koh-i-Nor')
handle = Handle('Brauberg')
pen = Pen ('Parker')
pencil.draw()
pen.draw()
handle.draw()

