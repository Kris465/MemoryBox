predlogenie = input("Введите прдложение: ")
n = "Нн"
n_kol = sum(1 for c in predlogenie if c in n)
m = "Мм"
m_kol = sum(1 for c in predlogenie if c in m)
if m > n:
    print("М больше чем н")
elif n > m:
    print("Н больше чем м")
else:
    print("Они равны")
