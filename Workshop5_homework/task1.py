# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

def abv_func():
    text = input("Input text you wish to shuffle: ")
    num = int(input("Input the number of mixed words: "))
    ls = ["".join(random.choice(text) for i in range(0, len(text))) for k in range(num)]
    print(ls)
    looking_for = input("Which word would you like to delete? ")
    
    for i in range(num):
        if looking_for in ls:
            ls.remove(looking_for)
        
    if len(ls) == num:
        print("There isn't such word")
    
    print(ls)

abv_func()
