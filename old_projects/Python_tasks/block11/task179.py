m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

new_m = []
for i in range(6):
    new_m.append(m[i])
    new_m.append(m[11 - i])

print(new_m)
