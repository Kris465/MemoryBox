def find_words(source_word, target_words):
    source_letters = list(set(source_word))

    found_words = []

    for word in target_words:

        if all(letter in source_letters for letter in word):
            found_words.append(word)

    return found_words


source_word = 'вертикаль'
target_words = ['тир', 'ветка']

result = find_words(source_word, target_words)
print("Найденные слова:", result)
