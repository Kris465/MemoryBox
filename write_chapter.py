def write(text, name):
    with open(f"{name}.txt", "w", encoding="utf-8") as file:
        file.write(text)
