def generate_sequence(n, K):
    sequence = []
    a = 1
    for k in range(1, n+1):
        a = K * a + 1 / k
        sequence.append(a)
    return sequence


n = int(input("Введите число n: "))
K = int(input("Введите число K: "))
print(generate_sequence(n, K))
