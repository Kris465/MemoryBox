def is_in_arithmetic_progression(n, f, s):
    if s == 0:
        return n == f
    k = (n - f) / s
    return k.is_integer() and k >= 0


n = int(input("Введите число n: "))
f = int(input("Введите первый член прогрессии f: "))
s = int(input("Введите шаг s: "))

if is_in_arithmetic_progression(n, f, s):
    print(f"Число {n} является членом арифметической прогрессии")
else:
    print(f"Число {n} не является членом арифметической прогрессии")
