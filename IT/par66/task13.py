def generate_words(current_word, length):
    if len(current_word) == length:
        print(current_word)
        return
    for char in 'abcdefghijklmnopqrstuvwxyz':
        generate_words(current_word + char, length)
        length = int(input("Введите длину слова: "))


generate_words("", length)
