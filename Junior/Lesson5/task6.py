name = input("Введите имя:")
surname = input("Введите фамилию: ")
movies = []

while True:
    movie = input("Введите любимый фильм или exit: ")
    movies.append(movie)
    if movie == 'exit':
        break

print(f"{name} {surname} говорит, что Человек Паук любит {movies}")
with open('spider_man.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} любит {movies}")
