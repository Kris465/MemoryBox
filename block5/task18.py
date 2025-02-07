def calculate_z(a):
    t = 4 * a
    z = 3.5 * t**2 - 7 * t + 16
    return z


for a in range(2, 18):
    z = calculate_z(a)
    print(f'a = {a}, z = {z}')
