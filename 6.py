from itertools import count, cycle

for el in count(3):
    if el ==11:
        break
    print(el)

my_list = ["весна", "лето", "осень", "зима"]
years = 0
for el in cycle(my_list):
    if years ==11:
        break
    years += 1
    print(el)
