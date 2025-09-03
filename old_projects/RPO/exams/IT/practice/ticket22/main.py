import random

letters = list('ABCDEFGHIJKLMNO_')


def print_board(letters):
    """Функция для вывода игрового поля"""
    for i in range(0, len(letters), 4):
        print(" ".join(letters[i:i+4]))


def move(direction, letters):
    """Функция для перемещения пустой ячейки"""
    index = letters.index('_')

    if direction == 'up':
        if index < 4:
            return False
        swap_index = index - 4
    elif direction == 'down':
        if index >= 12:
            return False
        swap_index = index + 4
    elif direction == 'left':
        if index % 4 == 0:
            return False
        swap_index = index - 1
    elif direction == 'right':
        if index % 4 == 3:
            return False
        swap_index = index + 1
    else:
        return False

    letters[index], letters[swap_index] = letters[swap_index], letters[index]
    return True


def check_win(letters):
    correct_order = list('ABCDEFGHIJKLMN_O')
    return letters == correct_order


def main():
    random.shuffle(letters)

    while not check_win(letters):
        print_board(letters)

        command = input("Ваш ход (w/a/s/d): ").strip().lower()

        if command in ['w', 'a', 's', 'd']:
            command_map = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}
            success = move(command_map[command], letters)

            if not success:
                print("Неверный ход!")
        else:
            print("Неправильная команда! Используйте w/a/s/d.")

    print_board(letters)
    print("Поздравляем! Вы победили!")


if __name__ == "__main__":
    main()
