def is_a_less_than_b(n, a, b):
    return str(n).count(str(a)) < str(n).count(str(b))


n = 1090
a = 0
b = 9
print(is_a_less_than_b(n, a, b))
