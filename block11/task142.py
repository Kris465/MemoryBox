a = [...]

if not a:
    print("Массив пуст")
else:
    max_abs_val = max(abs(x) for x in a)
    for i in range(len(a)):
        if abs(a[i]) == max_abs_val:
            a[i] *= -1
            break

print("Измененный массив:", a)
