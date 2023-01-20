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

import random

def jokes():
    num = int(input("How many jokes would you like to get? "))
    unique = input("Would you like to get unique jokes? Input 'yes' for agreement: ")
    if unique == "yes" or "Yes":
        unique = True
    else: unique = False

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    n, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
 
    random.shuffle(n)
    random.shuffle(adv)
    random.shuffle(adj)
    ls = []

    if unique == True and num < len(nouns):
        ls = list(zip(n, adv, adj))
        for i in range(0, num):
            print(ls[i])
    elif unique == True and num > len(nouns):
        print("Your number is bigger than I can generate.")
    else: 
        for i in range(0, num):
            k = random.randint(1, 4)
            ls.append(n[k])
            ls.append(adv[k + 1])
            ls.append(adj[k - 1])

jokes()
