def convert_temperature(T_C):
    T_F = T_C * 1.8 + 32
    T_K = T_C + 273.15
    return T_F, T_K


T_C = float(input("Введите температуру по Цельсию: "))

T_F, T_K = convert_temperature(T_C)

print(f"Температура по Фаренгейту: {T_F}")
print(f"Температура по Кельвину: {T_K}")