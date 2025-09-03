def is_member(n, f, s):
    if s == 0:
        return n == f
    else:
        return (n - f) % s == 0 and (n - f) // s >= 0


n = 15
f = 3
s = 4

if is_member(n, f, s):
    print(f"{n} является членом арифметической прогрессии с первым членом {f} и шагом {s}")
else:
    print(f"{n} не является членом арифметической прогрессии с первым членом {f} и шагом {s}")
