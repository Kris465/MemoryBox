# 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# in
# 10 True

# out

# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']

# in
# 10 False

# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']

from random import choice, randrange

def jokes():
    num = int(input("How many jokes would you like to get? "))
    unique = bool(input("Would you like to get unique jokes? Input 'True' for agreement: "))

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    n, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    lst = []
    list_min = min(n, adv, adj)

    for i in range(len(list_min) % num if unique else num):
        number = randrange(len(list_min))
        lst.append(f"{n.pop(number)} {adv.pop(number)} {adj.pop(number)}" if unique else f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")

    print(lst) 

jokes()
