# "C:/Users/Admin/Desktop"

adres = input(str("Введите адрес файла: "))

parts = adres.split("/")
for part in parts:
    print(part)
