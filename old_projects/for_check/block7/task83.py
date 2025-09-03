def find_best_team(a):
    sorted_results = sorted(enumerate(a), key=lambda x: x[1])
    best_four_indices = [index for index, _ in sorted_results[:4]]
    return best_four_indices


def add_number_to_list(results):
    while True:
        user_input = input("Введите число\
 (например, 12.36 для остановки напишите 'stop'): ")

        if user_input.lower() == 'stop':
            break

        try:
            number = float(user_input)
            results.append(number)
            print(f"Число {number} успешно добавлено в список.")
        except ValueError:
            print("Ошибка! Введено некорректное значение. Попробуйте еще раз.")


n = 6
results = []
add_number_to_list(results)
best_team = find_best_team(results)
print(best_team)
