from random import choice


def random_choice():
    items = input("Введите элементы через запятую: ").split(',')
    chosen_item = choice(items).strip()
    
    print(f"Случайно выбранный элемент: {chosen_item}")


random_choice()
