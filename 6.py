def int_func(word):
    b_word = word[0].upper() + word[1:].lower()
    return b_word

a = input("введите слово:")
print(int_func(a))

b = input("введите предложение:")
c_list = b.split()
for el in c_list:
    print(int_func(el))
