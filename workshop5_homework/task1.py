# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def delete_letters():
    d_text = input("Input words you wish to delete from the text: ")
    lst = []

    with open("task1.txt", "r") as file:
        line = file.readline()
        while line:
            lst = [i for i in line.split() if d_text not in i]
            print(line, end="")
            print(" ".join(lst))
            line = file.readline()

delete_letters()



