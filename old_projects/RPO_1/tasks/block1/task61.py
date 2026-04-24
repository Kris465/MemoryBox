while True:
    try:
        a = float(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка: пожалуйста, введите корректное число.")
    except KeyboardInterrupt:
        print("\nВвод прерван пользователем.")
        exit()

res_a = a * 4
res_b = (a * a) * 6
res_v = (a * a * a) * 7
res_g = (a * a) * 8
res_d = (a ** 4) * 9
res_e = (a ** 4) * 10
res_j = (a ** 6) * 13
res_z = (a ** 6) * 15
res_i = (a ** 6) * 7
res_k = (a ** 6) * 7
res_l = (a ** 7)

print(res_a)
print(res_b)
print(res_v)
print(res_g)
print(res_d)
print(res_e)
print(res_j)
print(res_z)
print(res_i)
print(res_k)
print(res_l)