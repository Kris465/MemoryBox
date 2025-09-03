array = [10, -4, 12, 56, -4, -89]

sign_changes = 0

for i in range(1, len(array)):
    if (array[i] > 0 and array[i-1] < 0) or (array[i] < 0 and array[i-1] > 0):
        sign_changes += 1

print(f"Количество изменений знака: {sign_changes}")
