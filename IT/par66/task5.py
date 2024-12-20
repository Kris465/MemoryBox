full_name = input("Введите ФИО: ")
last_name, first_name, patronymic = full_name.split()
initials = f"{first_name[0]}.{patronymic[0]}."
print(f"{initials} {last_name}")
