x = int(input("Введите возраст Тани: "))
y = int(input("Введите возраст Мити: "))

average_age = (x + y) / 2

difference_tanya = x - average_age
difference_mitya = x - average_age

print(f"Средний возраст: {average_age} лет.")
print(f"Возраст Тани отличается от среднего на {difference_tanya} лет")
print(f"Возраст Мити отличается от среднего на {difference_mitya} лет")
