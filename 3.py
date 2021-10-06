def my_func(n_1, n_2, n_3):
    sym_n = n_1 + n_2 + n_3
    min_n = min(n_1, n_2, n_3)
    return sym_n - min_n


a = int(input("число 1 :"))
b = int(input("число 2 :"))
c = int(input("число 3 :"))
print(my_func(a, b, c))
