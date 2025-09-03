num_cases = int(input("Введите количество дел: "))
cases = {}

for i in range(num_cases):
    title = input("Введите название дела: ")
    status = input("Введите статус (решено/не решено): ").lower()
    difficulty = int(input("Введите сложность дела (число): "))

    cases[title] = {
        'status': status,
        'difficulty': difficulty
    }

print("Дела, которые не решены и имеют сложность больше 5:")
for title, info in cases.items():
    if info['status'] == 'не решено' and info['difficulty'] > 5:
        print(f"- {title} (Сложность: {info['difficulty']})")
