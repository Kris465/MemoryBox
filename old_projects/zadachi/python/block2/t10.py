number = int(input("Введите двузначное число: "))
decyatki = number // 10
edinici = number % 10
summa = decyatki + edinici
multi = decyatki * edinici

print(f"Десятки: {decyatki}, единицы: {edinici}\n",
      f"сумма: {summa}, произведение: {multi}")
