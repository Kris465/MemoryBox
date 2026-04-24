import math

y = float(input())

hours = int(y // (math.pi / 6))

remaining_rad = y % (math.pi / 6)

minutes = int(remaining_rad // (math.pi / 360))


minute_angle = (hours * math.pi / 6 + remaining_rad) * 12 % (2 * math.pi)

print(f"{minute_angle:.6f}")
print(hours, minutes)
