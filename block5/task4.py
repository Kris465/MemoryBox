print("Часть а)")
for i in range(10, 26):
    print(f"{i} {i + 0.4}")


print("\nЧасть б)")
for i in range(25, 36):
    second_number = i + 0.5
    third_number = second_number - 0.2
    print(f"{i} {second_number:.1f} {third_number:.1f}")
