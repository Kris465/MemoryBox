def rearrange_word(word, s, k):
    if s < 0 or k < 0 or s >= len(word) or k >= len(word) or s >= k:
        return "Некорректные значения s и k."
    return word[:s] + word[s + 1:k] + word[s] + word[k:]


word = input("Введите слово: ")
s = int(input("Введите номер позиции s (начиная с 0): "))
k = int(input("Введите номер позиции k (начиная с 0): "))

modified_word = rearrange_word(word, s, k)
print("Измененное слово:", modified_word)
