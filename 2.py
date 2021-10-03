a = input("Введите список:")
a_list = a.split()
a_len = len(a_list)
i = 0
while i < a_len -1:
    b = a_list[i]
    a_list[i] = a_list[i+1]
    a_list[i+1] = b
    i+= 2


print(a_list)
