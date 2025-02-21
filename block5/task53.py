num = int(input("Введите число: "))
num_str = str(num)

increasing = all(num_str[i] > num_str[i + 1] for i in range(len(num_str)-1))

if increasing:
    print("Последовательность цифр упорядочена по возрастанию справа налево")
else:
    print("Последовательность цифр не упорядочены по возрастанию")
