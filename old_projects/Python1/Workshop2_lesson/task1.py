# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

def n_func():
    for i in range(int(input("Input your number, please: "))):
        print((-3) ** i, end = ' ')

n_func()