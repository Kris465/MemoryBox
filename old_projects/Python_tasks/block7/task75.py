def count_max_apartments(people):
    max_people = max(people)
    return people.count(max_people)


people = [3, 5, 2, 5, 4]
result = count_max_apartments(people)
print(f"Количество квартир с наибольшим числом жильцов: {result}")
