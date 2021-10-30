
class TechStore:
    def __init__(self, techs):
        if not techs:
            techs = []
        self.techs = techs

    def __repr__(self):
        return f'{self.techs}'

    def tech_count(self, count=None):
        sum = 0
        for el in self.techs:
            sum += el.count
        return sum

    def add_tech(self, tech):
        self.techs.append(tech)
        print('!!!Store arrival!!!')

    def get_tech(self, tech, shop):
        if tech in self.techs:
            self.techs.remove(tech)
            shop.add_tech(tech)
        else:
            print('!!!This product is off!!!')

    def shop_return(self, tech, shop):
        if shop.return_tech(tech):
            self.techs.append(tech)
            print('Shop returns')

    def get_q(self,tech):
        try:
            if tech > 3:
                raise ValueError("Off limit!")
        except ValueError as err:
            print(err)


class Tech:
    def __init__(self, brand, count):
        self.brand = brand
        self.count = count

    def __repr__(self):
        return f'{self.brand}:{self.count}'


class Printer(Tech):
    def __init__(self, brand, count):
        super().__init__(brand, count)
        self.brand = brand
        self.count = count
        self.model = "Color"


class Xerox(Tech):
    def __init__(self, brand, count):
        super().__init__(brand, count)
        self.brand = brand
        self.count = count
        self.model = "Lazer"


class Scaner(Tech):
    def __init__(self, brand, count):
        super().__init__(brand, count)
        self.brand = brand
        self.count = count
        self.model = "Flatbed"


class Shop:
    def __init__(self, name, techs = None):
        if not techs:
            techs = []
        self.techs = techs
        self.name = name

    def __str__(self):
        return f'{self.techs}'

    def add_tech(self, tech):
        self.techs.append(tech)
        print('!!!New arrival!!!')

    def return_tech(self, tech):
        if tech in self.techs:
            self.techs.remove(tech)
            return True
        else:
            False


tech_1 = Printer('Asus', 1)
tech_2 = Xerox('Philips', 6)
tech_3 = Scaner('Samsung', 2)
tech_4 = Scaner('Acer', 4)
tech_5 = Xerox('Acer', 8)
shop = Shop('TechnoPort', [tech_3])
store_1 = TechStore([tech_1, tech_2, tech_4])
print(store_1)
print(store_1.tech_count())
store_1.add_tech(tech_5)
print(store_1)
store_1.get_tech(tech_1, shop)
print(store_1)
store_1.get_tech(tech_2, shop)
print(shop)
print(store_1)
