def custom_replace(input_string, search_word, replace_word):
    # Приводим строки к нижнему регистру для регистронезависимого поиска
    lower_input = input_string.lower()
    lower_search = search_word.lower()

    # Длина слова для поиска
    search_length = len(search_word)

    # Результирующая строка
    result = []

    # Индекс для итерации по строке
    i = 0

    while i < len(input_string):
        # Проверяем, совпадает ли подстрока с искомым словом
        if lower_input[i:i + search_length] == lower_search:
            # Если совпадает, добавляем замену в результат
            result.append(replace_word)
            # Пропускаем длину искомого слова
            i += search_length
        else:
            # Если не совпадает, добавляем текущий символ в результат
            result.append(input_string[i])
            i += 1

    return ''.join(result)


# Пример использования
input_string = "cat runs to another cat"
search_word = "cat"
replace_word = "bull"

output = custom_replace(input_string, search_word, replace_word)
print(output)
