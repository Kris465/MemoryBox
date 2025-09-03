
weights = [list(map(int, input("Введите массив: ").split()))]


min_weight = None
max_weight = None

for weight in weights:
    if min_weight is None or weight < min_weight:
        min_weight = weight
    if max_weight is None or weight > max_weight:
        max_weight = weight


result = max_weight > 2 * min_weight

print(f"Вес самого тяжелого превышает массу \
    самого легкого более чем в 2 раза: {result}")
