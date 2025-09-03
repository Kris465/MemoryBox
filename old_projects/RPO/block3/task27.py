x = int(input("Введите число: "))
y = int(input("Введите число: "))

if x > 2 and y > 3:
    print("а) True")

if x > 1 or y > -2:
    print("б) True")

if x >= 0 and y < 5:
    print("в) True")

if x > 3 or x < -1:
    print("г) True")

if x > 3 and x < 10:
    print("д) True")

if not (x > 2):
    print("е) True")

if not (x > 0 and x < 5):
    print("ж) True")

if 10 < x <= 20:
    print("з) True")

if 0 < y <= 4 and x < 5:
    print("и) True")
