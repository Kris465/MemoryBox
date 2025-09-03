# 5. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

def check_num():
    number = int(input("Input your number: "))
    if number % 5 == 0 and number % 10 == 0 or number % 15 == 0:
        if number % 30 != 0:
            print("Yes")
        else: print("No")
    else: print("Something unexpected happened")

check_num()