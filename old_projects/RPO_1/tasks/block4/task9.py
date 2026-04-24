def quick_compare(kmh, ms):
    """Быстрое сравнение в одну строку"""
    kmh_from_ms = ms * 3.6
    return "км/ч больше" if kmh > kmh_from_ms else "м/с больше" \
        if kmh_from_ms > kmh else "скорости равны"


test_cases = [(36, 10), (100, 30), (18, 5), (72, 20)]

for kmh, ms in test_cases:
    result = quick_compare(kmh, ms)
    print(f"{kmh} км/ч vs {ms} м/с: {result}")
