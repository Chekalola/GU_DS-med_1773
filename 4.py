num_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
with open("fourth_file.txt") as file, open("file_4.txt",'w') as file_4:
    content = file.readlines()
    for line in content:
        nums = line.split()
        rus_nums = num_dict.get(nums[0])
        file_4.write(f"{line.replace(nums[0], rus_nums)}")

