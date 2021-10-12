with open("third_file.txt") as file:
    content = file.readlines()
    surname_dict = {}
    sum_salary = 0
    num = 0
    for item in content:
        info = item.split()
        surname_dict.update({info[0]: int(info[1])})
        sum_salary += int(info[1])
        num += 1
print(f"av_salary :{sum_salary / num}")
for key, value in surname_dict.items():
    if value < 20000:
        print(f"salary<20000:{key}")

