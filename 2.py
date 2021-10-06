def name_dict(name, surname, date, place, email, phone):
    return f" {name},{surname},{date},{place},{email},{phone}"


n = input("name :")
s = input("surname :")
d = input("data :")
p = input("place :")
e = input("email :")
p = input("phone :")
print(name_dict(name=n, surname=s, date=d, place=p, email=e, phone=p))
