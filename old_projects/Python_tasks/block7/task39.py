import math

def calculate_hit_percentage(n, projectiles, R, H):
    g = 9.8
    hits = 0

    for v_0, phi in projectiles:
        phi_rad = math.radians(phi)

        t = R / (v_0 * math.cos(phi_rad))
        y = (v_0 * t * math.sin(phi_rad)) - (0.5 * g * t**2)

        if abs(y - H) < 1e-6:
            hits += 1

    hit_percentage = (hits / n) * 100
    return hit_percentage

n = int(input("Введите количество снарядов: "))
projectiles = []

for i in range(n):
    v_0, phi = map(float, input(f"Введите скорость и угол для {i + 1}-го снаряда (пример ввода: 14 66): ").split())
    projectiles.append((v_0, phi))

R = float(input("Введите расстояние до цели R: "))
H = float(input("Введите высоту цели H: "))

percentage = calculate_hit_percentage(n, projectiles, R, H)
print(f"Процент попадания снарядов в цель: {percentage:.2f}%")
