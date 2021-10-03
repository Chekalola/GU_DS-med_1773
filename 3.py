month_num =(input("Номер месяца:"))
a = "зима"
b = "весна"
c = "лето"
d = "осень"
month_dict = {"1": a, "2": a, "3": b, "4": b, "5": b, "6": c, "7": c, "8": c, "9": d, "10": d, "11": d, "12": d}
print(month_dict[month_num])

month_list = [a, a, b, b, b, c, c, c, d, d, d, a]
print(month_list[int(month_num) - 1])







