# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


def remove_duplicates(lst):
    return list(set(lst))


# my_list = list(map(int, input("Cписок: ").split()))
my_list = input("Список: ").split()
print(remove_duplicates(my_list))
