from random import randint

my_list = sorted([randint(1, 1000) for i in range(100)], reverse=True)
print(my_list)

a = int(input("Введите число а: "))
try:
    print(my_list.index(a))
except ValueError:
    print("Этого числа нет с списке")
