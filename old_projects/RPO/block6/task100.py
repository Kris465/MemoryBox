# a) В каком году урожайность превысит 22 центнера с гектара?
initial_yield = 20
yield_increase = 0.02
target_yield = 22

year = 1
while True:
    current_yield = initial_yield * (1 + yield_increase) ** (year - 1)
    if current_yield > target_yield:
        break
    year += 1

print(f"Урожайность превысит 22 центнера с гектара в {year} году.")

# б) В каком году площадь участка станет больше 120 гектаров?
initial_area = 100
area_increase = 0.05
target_area = 120

year = 1
while True:
    current_area = initial_area * (1 + area_increase) ** (year - 1)
    if current_area > target_area:
        break
    year += 1

print(f"Площадь участка станет больше 120 гектаров в {year} году.")

# в) В каком году общий урожай, собранный за все время, превысит 800 центнеров?
initial_area = 100
area_increase = 0.05
initial_yield = 20
yield_increase = 0.02
target_total_yield = 800

year = 1
total_yield = 0
while True:
    current_area = initial_area * (1 + area_increase) ** (year - 1)
    current_yield = initial_yield * (1 + yield_increase) ** (year - 1)
    current_total_yield = current_area * current_yield
    total_yield += current_total_yield
    if total_yield > target_total_yield:
        break
    year += 1

print(f"Общий урожай превысит 800 центнеров в {year} году.")
