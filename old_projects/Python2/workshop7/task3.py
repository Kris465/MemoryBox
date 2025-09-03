# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def mixer(num_file, name_file, result_file):
    with open(num_file, 'r+') as f1,\
         open(name_file, 'r+', encoding="UTF-8") as f2,\
            open(result_file, 'w+', encoding="UTF-8") as f3:
        nums = [line.strip().split("|") for line in f1.readlines()]
        names = [line.strip() for line in f2.readlines()]
        name_len = len(names)
        for i, v in enumerate(nums):
            name_index = i % name_len
            result = int(v[0]) * float(v[1])
            if result < 0:
                f3.write(
                    names[name_index].lower() + ' ' + str(abs(result)) + '\n')
            else:
                f3.write(
                    names[name_index].upper() + ' ' + str(round(result)) + '\n'
                    )


mixer("task1.txt", "task2.txt", "task3.txt")
