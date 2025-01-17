la = int(input("Введите размер 1a см: "))
wa = int(input("Введите размер 2a см: "))
ha = int(input("Введите размер 3a см: "))
lb = int(input("Введите размер 1b см: "))
wb = int(input("Введите размер 2b см: "))
hb = int(input("Введите размер 3b см: "))


suitcase_combinations = [
    (la, wa, ha),
    (la, ha, wa),
    (wa, la, ha),
    (wa, ha, la),
    (ha, la, wa),
    (ha, wa, la)
]


box_combinations = [
    (lb, wb, hb),
    (lb, hb, wb),
    (wb, lb, hb),
    (wb, hb, lb),
    (hb, lb, wb),
    (hb, wb, lb)
]


for sc in suitcase_combinations:
    for bc in box_combinations:
        if sc[0] >= bc[0] and sc[1] >= bc[1] and sc[2] >= bc[2]:
            print("Коробка может быть помещена в чемодан.")
            exit()


print("Коробка не может быть помещена в чемодан.")
