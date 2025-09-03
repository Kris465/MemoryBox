a = 14
st = ''
while a > 0:
    ost = a % 2 # получение остатка
    st = str(ost) + st
    a = a // 2 
print(st)

a = 14
print(bin(a[2:3])) #[2:] указать до самого конца

