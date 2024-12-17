number = int(input('Введите трехзначное число: '))
sto = number//100
des = (number//10) % 10
ed = number % 10
sum = sto + des + ed
print(f'число единиц = {ed}, число десятков = {des}, а сумма равна = {sum}')
