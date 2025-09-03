v = int(input("Введите объем v: "))
parallelepipeds = [
    (i, j, v // (i * j))
    for i in range(1, int(v**0.5) + 1)
    for j in range(1, int(v**0.5) + 1)
    if v % (i * j) == 0
]
print("Разные параллелепипеды:", parallelepipeds)


unique_parallelepipeds = {
    tuple(sorted((i, j, v // (i * j))))
    for i in range(1, int(v**0.5) + 1)
    for j in range(1, int(v**0.5) + 1)
    if v % (i * j) == 0
}
print("Уникальные параллелепипеды:", unique_parallelepipeds)
