class MyExeption(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt
s_1 = int(input("Введите делимое:"))
s_2 = int(input("Введите делитель:"))

try:
    if s_2 == 0:
        raise MyExeption("Division on Zero is forbidden!")
except MyExeption as err:
    print(err)
else:
    print(int(s_1/s_2))



