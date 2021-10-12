with open("fifth_file.txt", 'w') as file:
    file.write("2 6 8 7 3 5 0 9 6 4 2 1")

with open('fifth_file.txt')as file:
    content = file.read()
    content_str = content.split()
    sum_num = 0
    for el in content_str:
        sum_num += int(el)
print(sum_num)




