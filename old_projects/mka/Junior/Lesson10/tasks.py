import re


def find_word_occurrences(text, word):
    # Используем регулярное выражение для точного поиска слова
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, text)
    count = len(matches)
    return matches, count


# Чтение текста из файла
with open('Harry.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Запрос слова у пользователя
user_word = input("Введите слово для поиска: ")
occurrences, count = find_word_occurrences(text, user_word)

# Вывод результатов
# if count > 0:
#     print("Найденные слова:", occurrences)

print(f"Слово '{user_word}' упоминается {count} раз(а) в тексте.")
