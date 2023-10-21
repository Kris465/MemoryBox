# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = input("Введите текст: ")
words = sorted(text.split(), key=lambda w: w.lower())
max_len = len(words[-1])
for i, word in enumerate(words, 1):
    print("{:>{}d}. {}".format(i, len(str(len(words))), word.rjust(max_len)))