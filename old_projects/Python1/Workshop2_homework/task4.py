# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!


def sum_of_defined_nums():
    lst = []
    num_range = int(input("Input the range of empty list: "))
    multi = 0
    
    for i in range(-num_range, num_range + 1):
        lst.append(i)
    print(*lst)

    pos1 = int(input("Input the position of the first preferable number: "))
    pos2 = int(input("Input the position of the second preferable number: "))

    if pos1 > num_range - 1 or pos2 > num_range - 1 or pos1 < 0 or pos2 < 0:
        print("There isn't such kind of position in the list, try again.")
    else: 
        multi = lst[pos1 - 1] * lst[pos2 - 1]
        print(f"The answer is: {multi}")

sum_of_defined_nums()
