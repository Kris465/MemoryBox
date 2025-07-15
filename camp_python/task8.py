cheese = input("Сколько кусков сыра украл Джерри?")

if cheese.isdigit():
    cheese = int(cheese)
    print("Том мяукает: 'Мяу?! (Это не число!)'")
else:
    print("Джерри теперь спит на [число] сырных подушках!")
