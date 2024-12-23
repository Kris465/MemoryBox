import re


text = 'ЫШШО мышь крокодил анна кровь жажда программа'


text = re.sub(r'[,.?!]', '', text).lower()


words = text.split()


n = int(input("Введите количество букв искомого слова: "))


def has_adjacent_duplicates(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False


matching_words = [word for word in words if len(word) == n and has_adjacent_duplicates(word)]


print("Найденные слова:", matching_words)
print("Количество найденных слов:", len(matching_words))
