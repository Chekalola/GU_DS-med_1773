from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 * 5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, suit_list):
        sum = 0
        for suit in suit_list:
            sum += suit.consumption
        return sum

coat = Coat(34)
suit = Suit(1.78)
suit_list = [coat, suit]
print(coat.consumption)
print(suit.consumption)
print(suit.sum_consumption(suit_list))