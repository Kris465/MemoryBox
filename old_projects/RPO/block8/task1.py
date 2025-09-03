for _ in range(6):
    print("5 " * 6)

print()

for _ in range(4):
    print(" ".join(str(i) for i in range(1, 11)))

print()

for i in range(41, 81, 10):
    print(" ".join(str(j) for j in range(i, i + 10)))
