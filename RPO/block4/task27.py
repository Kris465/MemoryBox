num = int(input("Введите трёхзначное число: "))
one = (num // 100) % 10
two = (num // 10) % 10
three = num % 10
if one == two and one == three:
    print("Число является палиндромом")
elif two == one and two == three:
    print("Число является палиндромом")
elif three == one and three == two:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
