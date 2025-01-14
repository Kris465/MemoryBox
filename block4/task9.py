def compare_speeds(km_per_hour, m_per_second):
    mps_from_kph = km_per_hour * 1000 / 3600
    if mps_from_kph > m_per_second:
        print("Скорость {km_per_hour} км/ч больше, чем {m_per_second} м/с")
    elif mps_from_kph < m_per_second:
        print(f"Скорость {m_per_second} м/с больше, чем {km_per_hour} км/ч")
    else:
        print("Скорость равны")
