# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import sample

def list_of_words():
    count = int(input("Input the size of the list: "))
    lst = []
    word = input("Input your word, please: ")

    for i in range(count):
        temp = (sample(word, k=3))
        lst.append("".join(temp))
    print(lst)
    return lst

def index_num(nlist):
    find_word = input("Input the word that I have to find: ")

    if find_word in nlist:
        index_1 = nlist.index(find_word)
        print(nlist.index(find_word, index_1 + 1))
    else: print("-1")

index_num(list_of_words())
