# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

def salary():
    amount = int(input("Input your number: "))
    answer = []

    while amount > 0:
        if amount >= 25:
            answer.append(25)
            amount = amount - 25
        elif 25 > amount >= 10:
            answer.append(10)
            amount = amount - 10
        elif 10 > amount >= 3:
            answer.append(3)
            amount = amount - 3
        else:
            answer.append(1)
            amount = amount - 1
    
    print(*answer)

salary()