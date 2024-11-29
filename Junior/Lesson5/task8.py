name = input("Введите имя:")
surname = input("Введите фамилию: ")
quotes = []

while True:
    quote = input("Введите любимую цитату или exit: ")
    quotes.append(quote)
    if quote == 'exit':
        break

print(f"{name} {surname} любит цитаты Капитана Америки: {quotes}")
with open('captain_quotes.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} любит {quotes}")
