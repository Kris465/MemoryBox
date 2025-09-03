def last_index_of_100(n, b):
    for i in range(n - 1, -1, -1):
        if b[i] == 100:
            return i + 1  # Номера считаем с 1
    return None


n = 7
b = [10, 20, 100, 30, 100, 40, 50]
result = last_index_of_100(n, b)
print(result)
