name = input("Введите имя:")
surname = input("Введите фамилию: ")
movies = []

while True:
    movie = input("Введите любимый гаджет Железного человека или exit: ")
    movies.append(movie)
    if movie == 'exit':
        break

print(f"{name} {surname} говорит, что Железный человек любит {movies}")
with open('ironman_tech.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} любит {movies}")
