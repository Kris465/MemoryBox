chislo = int(input("Введите четырехзначное число: "))
a = chislo // 1000
b = chislo % 1000 // 100
c = chislo % 100 // 10
d = chislo % 10
print(f"Перестановка {d}{c}{b}{a}")
print(f"перестановка {b}{a}{d}{c}")
print(f"перестановка {a}{c}{b}{d}")
print(f"перестановка {c}{d}{a}{b}")
