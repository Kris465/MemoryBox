number = int(input("Введите трехзначное число: "))

ed = number % 10
des = (number // 10) % 10
sot = number // 100
suma = ed + des + sot
multi = ed * des * sot
print(f"Единиц: {ed}, десятков: {des}, сотен: {sot},\n",
      f"Сумма: {suma}, произведение: {multi}")
