def check_load_capacity(cargo_weights, capacity):
    while True:
        user_input = int(input("Введите вес груза,\
 для остановки напишите '0'): "))

        if user_input == 0:
            break

        try:
            cargo_weights.append(user_input)
            print(f"Груз весом: {user_input}, успешно добавлено в список.")
        except ValueError:
            print("Ошибка! Введено некорректное значение. Попробуйте еще раз.")
    total_weight = sum(cargo_weights)
    if total_weight > capacity:
        return f"Превышена! Общая масса: {total_weight} кг."
    else:
        return f"Не превышена. Общая масса: {total_weight} кг."


cargo_weights = []
capacity = int(input('Введите грузоподъемность грузовика: '))

result = check_load_capacity(cargo_weights, capacity)
print(result)
