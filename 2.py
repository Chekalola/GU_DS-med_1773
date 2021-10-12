with open("second_file.txt") as file:
    content = file.readlines()
    print(content)
    for index, el in enumerate(content):
        num = len(el.split())
        print(index+1, num)



