A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

Codition_a = (A > 100) and ()
Codition_b = (A % 2 == 0) != (8 % 2 == 0)
Codition_v = (A > 0) or (8 > 0)
Codition_g = (A % 3 == 0) and (B % 3 == 0) and (C % 3 == 0)
Codition_d = (A < 50) + (B < 50) + (C < 50) == 1
Codition_e = (A < 0) or (B < 0) or (C < 0)

print("Вывод примеров")
print(f"a) каждое из чисел А и В больше 100: {Codition_a}")
print(f"б) только одно из чисел А и В четное:{Codition_b}")
print((f"в) хотя бы одно из чисел А и В положительно:{Codition_v}"))
print((f"г) каждое из чисел А, В, С кратно трем:{Codition_g}"))
print((f"д) только одно из чисел А, В и С меньше 50:{Codition_d}"))
print((f"е) хотя бы одно из чисел А, В, С отрицательно:{Codition_e}"))
