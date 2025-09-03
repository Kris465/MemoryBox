num_ingredients = int(input("Сколько ингредиентов нужно для пирожка?"))
ingredients = []
for i in range(num_ingredients):
    ingredient_name = input(f"Введите название ингридиента {i + 1}: ")
    ingredients.append(ingredient_name)

for ingredient in ingredients:
    has_ingredient = input(f"Есть ли у вас {ingredient}? (да/нет):")
    if has_ingredient.lower() == "да":
        print(f"{ingredient} есть")
    else:
        print(f"{ingredient} нет")
