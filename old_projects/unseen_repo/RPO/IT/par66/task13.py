def generate_combinations(current, length):
    if len(current) == length:
        print(current)
        return

    for char in 'abcdefghijklmnopqrstuvwxyz':
        generate_combinations(current + char, length)


def main():
    length = int(input("Введите длину слова: "))
    generate_combinations("", length)


if __name__ == "__main__":
    main()
