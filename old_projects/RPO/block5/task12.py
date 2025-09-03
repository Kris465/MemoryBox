import math


p0 = 1.29
z = 1.25e-4


def calculate_density(h):
    return p0 * math.exp(-z * h)


print("| Высота (м) | Плотность (кг/м³) |")
print("|------------|--------------------|")
for h in range(0, 1100, 100):
    density = calculate_density(h)
    print(f"| {h:<10} | {density:.2f}            |")
