import json

company = {}
com_prof = 0
sum_prof = 0
with open("seven_file.txt") as file:
    content = file.readlines()
    for line in content:
        info = line.split()
        profit = int(info[2]) - int(info[3])
        company.update({info[0]: profit})
        if profit > 0:
            com_prof += 1
            sum_prof += profit

av_profit = sum_prof / com_prof
result = [company, av_profit]

with open("seven.json", 'w') as file:
    json.dump(result, file)
