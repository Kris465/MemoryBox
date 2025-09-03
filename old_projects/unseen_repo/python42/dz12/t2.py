def change_reserved_words():
    text = input("Введите текст: ")
    reserved_words = input(
        "Введите зарезервированные слова, разделенные запятыми: ").split(',')
    reserved_words = [word.strip() for word in reserved_words]

    for word in reserved_words:
        text = text.replace(word, word.upper())
    print("Измененный текст:")
    print(text)


change_reserved_words()
