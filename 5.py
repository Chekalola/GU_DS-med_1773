a = int(input("Введите элемент рейтинга:"))
r_list = [7, 5, 3, 3, 2]
vv = False

for index,item in enumerate(r_list):
    if a > item:
        r_list.insert(index, a)
        vv = True
        break

else:
    r_list.append(a)
print(r_list)