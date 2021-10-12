result = { }
with open("six_file.txt") as file:
    content = file.readlines()
    for line in content:
        info = line.split()
        hours = 0
        for el in info[1:]:
            if el != "-":
                num = "0"
                for i in el:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)
        result.update({info[0].strip(':'): hours})
print(result)
