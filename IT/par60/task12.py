## симончук ксюша

num = int(input("Введите число: "))

def perfect(num):
    spisok = []
    for i in range(1, num):
        if num % 1 == 0:
            spisok.append(i)
    return sum(spisok) == num


print(perfect(num))