# Начальные условия
area = 100  # гектаров
yield_per_hectare = 20  # центнеров с гектара
total_yield = 0  # общий урожай за все годы

# Процент увеличения
area_increase_percent = 0.05
yield_increase_percent = 0.02

# Инициализация счетчика лет
year = 1

# Переменные для отслеживания условий
yield_exceeded = False
area_exceeded = False
total_yield_exceeded = False

# Цикл для поиска всех условий
while not (yield_exceeded and area_exceeded and total_yield_exceeded):
    # Урожайность текущего года
    current_yield = area * yield_per_hectare
    total_yield += current_yield

    # Проверка условий
    if not yield_exceeded and yield_per_hectare > 22:
        yield_exceeded = True
        print(f"Год, когда урожайность превысит 22 центнера с гектара: {year}")

    if not area_exceeded and area > 120:
        area_exceeded = True
        print(f"Год, когда площадь участка превысит 120 гектаров: {year}")

    if not total_yield_exceeded and total_yield > 800:
        total_yield_exceeded = True
        print(f"Год, когда общий урожай превысит 800 центнеров: {year}")

    # Обновление значений на следующий год
    area *= (1 + area_increase_percent)
    yield_per_hectare *= (1 + yield_increase_percent)
    year += 1
