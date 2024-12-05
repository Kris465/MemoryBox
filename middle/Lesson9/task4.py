def dinosars():
    dinosars = {}
    while True:
        name = input("Введите имя динозавра: ")
        if name == 'exit':
            break
        kind = input("Введите вид динозавра: ")
        age = int(input("Введите возраст динозавра (млн. лет): "))
        if age > 65:
            die = "вымер"
        else:
            die = "живой"
        dinosars.update({name: [kind, age, die]})

        if name == 'exit':
            break

    return dinosars


print(dinosars())
