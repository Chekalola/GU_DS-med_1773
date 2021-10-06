def sum_n(n_str,stop):
    n_list = n_str.split()
    sum_list = 0
    for el in n_list:
        if el == stop:
            break
        sum_list += int(el)
    return sum_list


stop = "$"
fin = False
sum = 0
while fin == False:
    nums = input("Введите числа через пробел:")
    sum += sum_n(nums,stop)
    fin = stop in nums
    print(sum)




