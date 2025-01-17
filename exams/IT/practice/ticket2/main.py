from random import randint


def triple_characters(s):
    return ''.join([char * 3 for char in s])


original_string = input('Введите ваше сообощение: ')
tripled_string = triple_characters(original_string)
a = []
for f in range(10):
    flag = randint(1, len(original_string))
i = 0
k = randint(0, 2)


while i < len(tripled_string):
    b = tripled_string[i:i+4]
    if k == 0:
        a.append(b[:-1])
    elif k == 1:
        a.append(b[1:])
    else:
        e = b[0:2]
        w = b[3:5]
        a.append(e + w)
    i += 4

redflag = ''.join(a) + ' '
greenflag = []
for i in range(0, len(redflag) - 1):
    if redflag[i] != redflag[i+1]:
        greenflag.append(redflag[i])

print(redflag)
print(''.join(greenflag))
