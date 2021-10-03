a = input("Введите список:")
a_list = a.split()
b = len(a)
i = 0
while i < b -1:
    a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    i+= 2


print(a_list)
