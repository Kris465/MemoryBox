def triangle_type(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "Треугольник не существует"

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        type_desc = "Остроугольный"
    elif sides[0]**2 + sides[1]**2 > sides[2]**2:
        type_desc = "Тупоугольный"
    else:
        type_desc = "Тупоугольный"

    return type_desc


def triangle_properties(a, b, c):
    if a == b == c:
        return "Равностороний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"


a = float(input())
b = float(input())
c = float(input())

type_result = triangle_type(a, b, c)
if type_result == "Треугольник не существует":
    print(type_result)
else:
    properties_result = triangle_properties(a, b, c)
    print(type_result)
    print(properties_result)
