slovo = input("Введите слово: ")
predlozhenie = input("Введите предложение: ")
kolichestvo = 0
for i in predlozhenie.split():
    if slovo in predlozhenie:
        kolichestvo += 1
print(kolichestvo)
