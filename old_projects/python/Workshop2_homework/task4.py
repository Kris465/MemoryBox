# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random


def multiplication():
    infile = open("file.txt", "w")
    size = int(input("How many numbers would you like to put in file: "))
            
    for i in range(size):
        infile.write(f"{str(random.randint(-size, size + 1))}\n")
    
    infile.close()
    print("Numbers were written in a file.")

    position1 = int(input(f"Input the first position in {size}: "))
    position2 = int(input(f"Input the second position in {size}: "))

    inform = open("file.txt","r")
    lst = inform.read().splitlines()
    print("You list is: ")
    print(lst)
    multi = int(lst[position1 - 1]) * int(lst[position2 - 1])
    print(multi)


multiplication()