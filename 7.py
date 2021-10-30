class MyComplex:
    def __init__(self, real, imag):
        self.imag = imag
        self.real = real

    def __str__(self):
        return f'{self.imag}+{self.real}j'

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return MyComplex(real, imag)

    def __mul__(self, other):
        return MyComplex(self.real*other.real - self.imag*other.imag,
                         self.imag*other.real + self.real*other.imag)
x = MyComplex(5, 2)
y = MyComplex(8, -3)

print(x + y)
print(x * y)
