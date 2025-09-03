def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


num1 = 48
num2 = 180
gcd_value = gcd(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {gcd_value}")
