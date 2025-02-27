## а)
multiples_of_13 = [i for i in range(1, 100) if i % 13 == 0]
print(multiples_of_13)
## б)
for i in range(1, 100):
    if i % 13 == 0:
        print(i)