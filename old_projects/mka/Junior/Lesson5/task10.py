name = input("Введите имя:")
surname = input("Введите фамилию: ")
activities = []

while True:
    activity = input("Введите любимый вид спорта или exit: ")
    activities.append(activity)
    if activity == 'exit':
        break

print(f"{name} {surname} считает, что Черная вдова любит заниматься {activities}")
with open('blackwidowsports.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} любит {activities}")
