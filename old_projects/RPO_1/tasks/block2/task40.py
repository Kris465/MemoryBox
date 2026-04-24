y = float(input())

hours = int(y // 30)

remaining_degrees = y % 30

minutes = int(remaining_degrees // 0.5)

print(hours, minutes)