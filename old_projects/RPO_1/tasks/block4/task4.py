def determine_area(x, y):

    if y < x:
        return "Область I"
    else:
        return "Область II"


x = float(input("Введите x: "))
y = float(input("Введите y: "))

result = determine_area(x, y)
print(result)
