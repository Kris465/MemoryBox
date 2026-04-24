districts = [
    (120, 25),  # район 1
    (80, 32),   # район 2
    (150, 18),  # район 3
    (200, 22),  # район 4
    (90, 29),   # район 5
    (130, 26),  # район 6
    (170, 20),  # район 7
    (110, 30),  # район 8
    (95, 27),   # район 9
    (140, 24)   # район 10
]

total_harvest = sum(area * yield_per_ha for area, yield_per_ha in districts)

total_area = sum(area for area, _ in districts)

average_yield = total_harvest / total_area

print(f"Общий сбор пшеницы: {total_harvest:.2f} ц")
print(f"Средняя урожайность по области: {average_yield:.2f} ц/га")
