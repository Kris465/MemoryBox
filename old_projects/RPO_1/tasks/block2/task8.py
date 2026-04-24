k = int(input()) 


n_a = k % 7
if n_a == 0:
    n_a = 7
print(n_a)


n_b = (k + 1) % 7
if n_b == 0:
    n_b = 7
print(n_b)

d = int(input("Введите номер дня недели 1 января (от 1 до 7): "))
n_v = (k - 1 + d) % 7
if n_v == 0:
    n_v = 7
print(n_v)
