x = 1
y = -1
print(f"а) {((x ** 2) + (y ** 2)) <= 4}")

x = 1
y = 2
print(f"б) {(x >= 0) or ((y ** 2) != 4)}")

x = 1
y = 2
print(f"в) {(x >= 0) and ((y ** 2) != 4)}")

x = 2
y = 1
print(f"г) {((x * y) != 0) and (y > x)}")

x = 2
y = 1
print(f"д) {((x * y) != 0) or (y < x)}")

x = 2
y = 1
print(f"e) {((x * y) < 0) and (y > x)}")

x = 1
y = 2
print(f"ж) {((x * y) < 0) or (y > x)}")
