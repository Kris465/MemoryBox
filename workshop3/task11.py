# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1][1]/x[1][0],
                          reverse=True)
    backpack = {}
    weight = 0

    for item in sorted_items:
        if weight + item[1][0] <= max_weight:
            backpack[item[0]] = item[1]
            weight += item[1][0]
    return backpack


items = {'палатка': (4, 100), 'спальник': (2, 50),
         'еда': (3, 25), 'вода': (1, 10)}
max_weight = 7
print(fill_backpack(items, max_weight))


# Для возврата всех возможных вариантов можно использовать рекурсию:
def fill_backpack_all(items, max_weight):
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1][1]/x[1][0],
                          reverse=True)
    backpacks = []

    def fill(backpack, weight, i):
        if i == len(sorted_items):
            backpacks.append(backpack)
            return
        item = sorted_items[i]
        if weight + item[1][0] <= max_weight:
            fill(backpack.copy(), weight + item[1][0], i+1)
            backpack[item[0]] = item[1]
            fill(backpack.copy(), weight + item[1][0], i+1)
        else:
            fill(backpack.copy(), weight, i+1)
    fill({}, 0, 0)
    return backpacks


items = {'палатка': (4, 100), 'спальник': (2, 50),
         'еда': (3, 25), 'вода': (1, 10)}
max_weight = 7
print(fill_backpack_all(items, max_weight))
