x_a = 1
y_a = 1
result_a = 2 * 2 * x_a * y_a * 4

x_b = 1
y_b = 2
result_b = (x_b == 0) or 2 * (y_b == 4)

x_v = 1
y_v = 2
result_v = (x_v == 0) and 2 * (y_v == 4)

x_g = 2
y_g = 1
result_g = (x_g * y_g == 0) and (y_g > x_g)

x_d = 2
y_d = 1
result_d = (x_d * y_d == 0) or (y_d < x_d)

x_e = 2
y_e = 1
result_e = (not (x_e * y_e < 0)) and (y_e > x_e)

x_zh = 1
y_zh = 2
result_zh = (not (x_zh * y_zh < 0)) or (y_zh > x_zh)

# Вывод результатов
print("а)", result_a)
print("б)", result_b)
print("в)", result_v)
print("г)", result_g)
print("д)", result_d)
print("е)", result_e)
print("ж)", result_zh)
