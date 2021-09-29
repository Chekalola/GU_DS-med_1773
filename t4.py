a = int(input("Введите число:"))
b = 1
while a > 0:

    if a % 10 > b:
        b = a % 10
        if b == 9:
            break
    a = a // 10

print(b)
