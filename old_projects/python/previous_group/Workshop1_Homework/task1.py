# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

try:
    def day_of_the_week():
        number = int(input("Input a day of the week, please: "))
        if number == 6 or number == 7:
            print("Yes")
        else: 
            print("No")
except:
    print("Week doesn't have such day. Try again.")

day_of_the_week()

