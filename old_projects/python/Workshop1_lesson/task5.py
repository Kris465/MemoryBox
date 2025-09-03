# Показать первую цифру дробной части числа

print(123 % 10) # Остаток от деления 3
print(123 // 100) # Целочисленное деление 1

a = 6.85
a = a * 10
print(a)
a = int(a)
print(a)
print(a % 10)

a = 6.385 # float
st = str(a)
print(st)
d = st.find(".")
print(st[d+1])