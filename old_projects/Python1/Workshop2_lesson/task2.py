# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

def amazing_func():
    lst = []
    num = int(input("Input your number: "))
    for i in range(1, num + 1):
        lst.append(3 * i + 1)
    print(*lst)

amazing_func()

# lst.insert(2, True) - вставляет, пересчитывает последующие
# lst.extend([11, 22]) - расширяет изначальный список 