def count_sentences():
    text = input("Введите текст: ")
    count_sentences = [s.strip() for s in text.split('.') if s.strip()]
    print(len(count_sentences))


count_sentences()
