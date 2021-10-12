with open("first_file.txt", "w") as file:
    line = input("Print your text: \n")
    while line:
        file.write(f"{line}\n")
        line = input("Print your text: \n")






