num = int(input("Введите трехзначное число:"))

poslednee = num % 10
crednee = (num // 10) % 10
pervoe = (num // 100) % 10

if poslednee > pervoe:
    print("Последнее число больше первого числа")
elif poslednee < pervoe:
    print("Первое число больше посдеднего числа")


if pervoe > crednee:
    print("Первое число больше второго числа")
elif pervoe < crednee:
    print("Второе число больше первого числа")


if crednee > poslednee:
    print("Второе число больше последнего числа")
elif poslednee < crednee:
    print("Последнее число больше второго числа")
