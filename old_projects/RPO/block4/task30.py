number = int(input("Введите трехзначное число: "))


def trehchislo(num):
    if 100 <= num <= 999:
        digits = [int(d) for d in str(num)]
        a = sum(digits)
        b = digits[0] * digits[1] * digits[2]

        odin = 10 <= a <= 99

        dva = 100 <= b <= 999

        tri = a > b

        chetire = a % 5 == 0

        pyat = (a != 0 and num % a == 0)

        return {
            "Сумма (а) двузначное": odin,
            "Произведение (b)": dva,
            "а больше произведения": tri,
            "Сумма кратна 5": chetire,
            "Сумма кратна а": pyat
        }
    else:
        return "Введите трехзначное число."


results = trehchislo(number)
print(results)
