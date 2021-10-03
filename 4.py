a = input("Введите предложение:")
b = list(a.split())

for index, item in enumerate(b):
    print(f"{index}.{item[:10]}")



