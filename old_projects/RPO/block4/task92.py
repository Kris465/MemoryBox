x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
if x < 1:
    print("Iчетвреть")
elif x > 1 and x < 5:
    print("II четверть")
elif x > 5:
    print("III четверть")
else:
    print("Граница")
