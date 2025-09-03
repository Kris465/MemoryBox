import math


def deg_to_rad(deg):
    return deg * math.pi / 180


for angle in range(2, 21):
    sine_value = math.sin(deg_to_rad(angle))
    print(f'sin({angle}) = {sine_value:.4f}')
