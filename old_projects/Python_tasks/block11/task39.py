array = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("Второй, четвертый и далее элементы:")
for i in range(1, len(array), 2):
    print(array[i])

print("\nТретий, шестой и далее элементы:")
for i in range(2, len(array), 3):
    print(array[i])
