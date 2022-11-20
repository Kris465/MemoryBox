# Здесь интерфейс
# Инпут возвращает список с одним действием. Следовательно, интерфейс должен не только получать список действий, но и располагать их в нужном порядке.


def get_value():
    print("Hello! Welcome to our caculator.")
    expression = input("Input your expression, please: ")
    kind_operation = input("For complex numbers input 1, for usual numbers input 2: ")

    if kind_operation == 1:
        reel_part = input("Input the reel or main part of the first complex number: ")
        imaginaire_part = input("Input the imaginaire part of the first complex number: ")
        sign = input("Input the sing of operation: ")
        reel_part1 = input("Input the reel or main part of the second complex number: ")
        imaginaire_part1 = input("Input the imaginaire part of the second complex number: ")
        data = [reel_part + imaginaire_part, sign, reel_part1 + imaginaire_part1]
    else:
        data = expression.split()

    return data, kind_operation


def output(result):
    try:
        if result.is_integer():
            print(f"Your result is:", int(result))
        elif isinstance(result, float):
            print(f"Your result is:", result)
        else: print(result)
    except:
        print(result)
