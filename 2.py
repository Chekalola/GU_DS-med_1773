
my_test_list = [item for index,item in enumerate(my_list[1:]) if my_list[index] < my_list[index + 1]]
print(my_test_list)