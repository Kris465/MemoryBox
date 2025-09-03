def reverse_substring(word, k, s):
    if k < s and 0 <= k < len(word) and 0 <= s < len(word):
        substring = word[k + 1:s]
        reversed_substring = substring[::-1]
        return word[:k + 1] + reversed_substring + word[s:]
    return word


slovo = input("Введите слово из 15 букв: ")

if len(slovo) == 15:
    k = int(input("Введите значение k (индекс первой буквы): "))
    s = int(input("Введите значение s (индекс последней буквы): "))
    if k < s:
        modified_word = reverse_substring(slovo, k, s)
        print("Измененное слово:", modified_word)
    else:
        print("Ошибка: k должно быть меньше s.")
else:
    print("Ошибка: слово должно содержать ровно 15 букв.")
