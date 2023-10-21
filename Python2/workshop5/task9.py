# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['Катя', 'Света', 'Олег', 'Дима']
rates = [100, 200, 300, 400]
bonuses = ['23.5%', '13%', '7.5%', '18%']

result = {name: rate * float(bonus.strip('%')) / 100
          for name, rate, bonus in zip(names, rates, bonuses)}

print(result)