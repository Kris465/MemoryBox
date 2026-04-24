from datetime import datetime


def compare_ages(birthdate1, birthdate2):
    date_format = "%Y-%m-%d"
    person1_age = datetime.strptime(birthdate1, date_format)
    person2_age = datetime.strptime(birthdate2, date_format)

    if person1_age < person2_age:
        return "Первый человек старше"
    elif person1_age > person2_age:
        return "Второй человек старше"
    else:
        return "Оба человека родились в один день"


birthdate1 = "1990-05-15"
birthdate2 = "1992-03-10"
result = compare_ages(birthdate1, birthdate2)
print(result)
