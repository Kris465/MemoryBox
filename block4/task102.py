x = int(input("Введите число: "))
y = int(input("Введите число: ")) 
print('I четверть' if x > 0 and y > 0 else 'II четверть' if x < 0 and y > 0 else 'III четверть' if x < 0 and y < 0 else 'IV четверть' )
