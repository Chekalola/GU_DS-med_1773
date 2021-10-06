def nums_division(num_1, num_2):
    if num_2 == 0:
        return "NONE Zero"
    if num_2 >0:
        return num_1 / num_2

n_1 = int(input("dividend:"))
n_2 = int(input("divisor:"))
print(nums_division(n_1, n_2))

