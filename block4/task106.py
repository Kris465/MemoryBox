month=int(input('Введите число месяца:\n'))

season = {'winter':[12 , 1, 2], 'spring':[3, 4, 5],/
           'summer':[6, 7, 8], 'autum':[9, 10, 11]}

for k, i in season.items():
        if month in i:
                print(k)
