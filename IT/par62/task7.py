from random import randint

a = []
for i in range(100): 
    a.append(randint(1000, 2000))
print(f"2)\n{a}\n")
for i in range(1, len(a), 2):
    first = a[i-1]
    second = a[i]
    a[i-1] = second
    a[i] = first
print(a)
