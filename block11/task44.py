victories = [5, 2, 0, 4, 1, 3, 2, 6, 0, 2, 4, 1, 3, 2, 5, 0, 1, 4, 2, 3]
print("Номера команд с менее чем тремя победами:")
for index in range(len(victories)):
    if victories[index] < 3:
        print(index + 1)
