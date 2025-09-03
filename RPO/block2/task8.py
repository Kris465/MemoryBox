while True:
    try:
        k = int(input("Введите число k так, чтобы оно было \
            больше или равно 1 и меньше или равно 365: "))
        if 1 <= k <= 365:
            break
        else:
            print("Значение должно быть в диапазоне \
                от 1 до 365. Попробуйте снова.")
    except ValueError:
        print("Введено некорректное значение. \
            Пожалуйста, введите целое число.")


days_of_week = {
    0: 'Воскресенье',
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота'
}


day_offset = k % 7
first_day = days_of_week.get(day_offset, '')
print(f"а) Если первый день — понедельник, то день \
    под номером {k} — это {first_day}.")


second_day_offset = (k + 1) % 7
second_day = days_of_week.get(second_day_offset, '')
print(f"б) Если первый день — вторник, то день \
    под номером {k} — это {second_day}.")
