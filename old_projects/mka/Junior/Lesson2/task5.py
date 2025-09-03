def rate_character():
    characters = ["Микки Маус", "Супермен", "Дональд Дак"]
    ratings = {}

    for character in characters:
        rating = int(input(f"Как вы оцениваете {character} (1-5): "))
        ratings[character] = rating

    print("Ваши оценки:")
    for character, rating in ratings.items():
        print(f"{character}: {rating}")


rate_character()
