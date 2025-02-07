import string

def get_text_statistics(text):
    words = text.split()
    word_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    unique_punctuation = set(char for char in text if char in string.punctuation)
    unique_punctuation_count = len(unique_punctuation)

    return {
        "word_count": word_count,
        "unique_word_count": unique_word_count,
        "punctuation_count": punctuation_count,
        "unique_punctuation_count": unique_punctuation_count
    }

def main():
    user_input = input("Введите текст: ")
    stats = get_text_statistics(user_input)
    
    print("\nСтатистика текста:")
    print(f"Количество слов: {stats['word_count']}")
    print(f"Количество уникальных слов: {stats['unique_word_count']}")
    print(f"Количество знаков препинания: {stats['punctuation_count']}")
    print(f"Количество уникальных знаков препинания: {stats['unique_punctuation_count']}")

if __name__ == "__main__":
    main()
