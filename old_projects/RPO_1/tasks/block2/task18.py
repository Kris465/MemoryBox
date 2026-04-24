from random import randint


number = input("Введите трехзначное число: ")

# a = number[0]
# b = number[1]
# c = number[3]

my_list = []


while len(my_list) < 6:
    temp_number = number[randint(0, 2)] + number[randint(0, 2)] + number[randint(0, 2)]
    new_temp_number = "".join(set(temp_number))
    if len(new_temp_number) == 3:
        if temp_number not in my_list:
            my_list.append(temp_number)
        else:
            continue
    else:
        continue

for line in my_list:
    print(line)
