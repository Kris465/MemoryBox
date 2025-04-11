one_surname = input("Введите первую фамилию: ")
two_surname = input("Введите вторую фамилию: ")

first_surname_result = len(one_surname)
second_surname_result = len(two_surname)

if first_surname_result > second_surname_result:
    print(f"{one_surname} содержит больше букв, чем фамилия {two_surname}")
elif second_surname_result > first_surname_result:
    print(f"{two_surname} содержит больше букв, чем фамлия {one_surname}")
