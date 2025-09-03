import re


sentence = input("Введите предложение: ")


matches = re.findall(r'нн', sentence)


if matches:
    print('Буквосочетания "нн":')
    for match in matches:
        print(match)
else:
    print('Нет буквосочетаний "нн" в предложении.')
