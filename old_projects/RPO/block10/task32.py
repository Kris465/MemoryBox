def is_palindrome(word):
    cleaned_word = word.strip().lower()
    return cleaned_word == cleaned_word[::-1]


def main():
    words = []
    for i in range(1, 4):
        word = input(f"Введите слово {i}: ")
        words.append(word)

    palindrome_found = False
    for word in words:
        if is_palindrome(word):
            palindrome_found = True
            break

    if palindrome_found:
        print("В одном из введённых слов есть палиндром.")
    else:
        print("Нет ни одного палиндрома среди введённых слов.")


if __name__ == "__main__":
    main()
