def get_correct_ending(age):
    if age % 10 == 1 and age != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and not 12 <= age <= 14:
        return 'года'
    else:
        return 'лет'


age = int(input("Введите ваш возраст (от 1 до 99): "))
print(f"Мне {age} {get_correct_ending(age)}")
