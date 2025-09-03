import re


def load_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_derivatives(text, world):
    pattern = r'\b' + re.escape(world) + r'\w * \ b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches


def main():
    file_path = input("Введите путь к файлу книги: ")

    try:
        text = load_book(file_path)
    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, проверьте путь.")
        return

    word = input("Введите слово для поиска : ")
    derivatives = find_derivatives(text, word)

    count = len(derivatives)

    with open('results.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(f"Слово: {word}\n")
        result_file.write(f"Количество вхождений: {count}\n")
        result_file.write("Производные слова: \n")
        for derivative in derivatives:
            result_file.write(f"{derivative}\n")

    print(f"Результаты записаны в файл results.txt. Найдено {count} \
          производных")


if __name__ == "__main__":
    main()
