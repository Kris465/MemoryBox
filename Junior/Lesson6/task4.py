def cookery_book():
    cookery_book = {}
    recipe = ""
    while recipe != 'exit':
        recipe = input("Введите имя спортсмена: ")
        ingredients = input("Введите достижение спортсмена: ")
        cookery_book.update({recipe: ingredients})

    return cookery_book


print(cookery_book())
