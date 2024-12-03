# Манираки Александр
def oreh(n):
    if n == 1:
        return 1
    else:
        cnt = 0
        for i in range(1, n + 1):
            cnt += oreh(n - i)
        return cnt


uno = int(input("Введите число uno: "))
print(f"Количество разложений: {oreh(uno)}")
