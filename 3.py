class Cell:
    def __init__(self,nums):
        self.nums = nums

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        sub_n = self.nums - other.nums
        if sub_n >0:
            return Cell(sub_n)
        else:
            print("Error")

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(self.nums // other.nums)

    def make_order(self, count):
        s = ""
        for i in range(self.nums // count):
            s += '*' * count + "\n"
        s += '*' * (self.nums % count) +'\n'
        return s

    def __str__(self):
        return f'{self.nums}'

cell_1 = Cell(30)
print(cell_1.make_order(5))
cell_2 = Cell(23)
print(cell_2.make_order(7))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)




