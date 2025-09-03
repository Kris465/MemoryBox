number = input('Введите натуральное число: ')

index_2 = number.find('2')
index_5 = number.find('5')

if index_2 == -1 and index_5 == -1:
    print("Цифры 2 и 5 отсутствуют.")
elif index_2 != -1 and (index_5 == -1 or index_2 < index_5):
    print("Цифра 2 расположена левее")
elif index_5 != -1 and (index_2 == -1 or index_5 < index_2):
    print("Цифра 5 расположена левее")
else:
    print("Цифры на одной позиции.")
