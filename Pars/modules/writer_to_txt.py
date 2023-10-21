def write_txt(name, data):
    with open(f"{name}.txt", "a", encoding="UTF-8") as file:
        file.write(data)
