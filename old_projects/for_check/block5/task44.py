mass1 = float(input("Введите массу первого предмета: "))
mass2 = float(input("Введите массу второго предмета: "))
mass3 = float(input("Введите массу третьего предмета: "))
mass4 = float(input("Введите массу четвертого предмета: "))


if 0 <= mass1 <= 100 and 0 <= mass2 <= 100 and 0 <= mass3 <= 100 and 0 <= \
        mass4 <= 100:

    total_score = mass1 + mass2 + mass3 + mass4

    print("Сумма всех предметов:", total_score)
