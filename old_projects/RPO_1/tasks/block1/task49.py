import math

a = 10
b = 6
alpha_deg = 30

alpha = math.radians(alpha_deg)
h = (a - b) * math.tan(alpha)
area = (a + b) / 2 * h

print(area)
