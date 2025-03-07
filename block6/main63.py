def check_for_twos(grades): 
    return 2 in grades


grades = [5, 4, 3, 5, 4, 2, 5, 4, 3, 5, 4, 5, 4, 3, 5, 4, 5, 4, 3, 5, 4, 5, 4, 3, 5, 4, 5, 4]
has_twos = check_for_twos(grades)

if has_twos:
    print("В списках есть двойки")
else:
    print("Двоек в списках нет")
