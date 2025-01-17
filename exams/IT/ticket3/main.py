value = int(input("Введите количество: "))
from_unit = input("Введите первую единицу измерения (байт, килобайт, \
    мегабайт, гигабайт)")
to_unit = input("Введите вторую единицу измерения (байт, килобайт,\
    мегабайт, гигабайт)")


def convert_units(value, from_unit, to_unit):
    units = {
        'байт': 1,
        'килобайт': 1024,
        'мегабайт': 1024 ** 2,
        'гигабайт': 1024 ** 3
    }

    if from_unit in units and to_unit in units:
        byteval = value * units[from_unit]
        convval = byteval / units[to_unit]
        return int(convval)


result = convert_units(value, from_unit, to_unit)

if result is not None:
    print(f'{value} {from_unit} = {result} {to_unit} ')
