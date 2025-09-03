cars = [15000, 20000, 25000, 30000]
motorcycles = [4000, 5000, 3000, 4500]


if all(car > 5000 for car in cars):
    print("Все авто дороже $5000.")
else:
    print("Есть авто дешевле $5000.")


if all(motorcycle < 5000 for motorcycle in motorcycles):
    print("Все мотоциклы дешевле $5000.")
else:
    print("Есть мотоциклы дороже $5000.")


avg_car = sum(cars) / len(cars)
avg_motor = sum(motorcycles) / len(motorcycles)


if avg_car > 3 * avg_motor:
    print(f"Ср. цена авто {avg_car:.2f} > 3x ср. цены мото {avg_motor:.2f}.")
else:
    print(f"Ср. цена авто {avg_car:.2f} <= 3x ср. цены мото {avg_motor:.2f}.")
