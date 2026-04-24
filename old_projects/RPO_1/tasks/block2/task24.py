
for c in range(10):
    for a in range(1, 10):
        for b in range(10):
 
            if 100 * c + 10 * a + b == 237:
                x = 100 * a + 10 * b + c
                print(f"Найденное число x: {x}")
                break
        else:
            continue
        break
    else:
        continue
    break