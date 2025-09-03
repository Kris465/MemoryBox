def find_max_apartment(people):
    max_people = max(people)
    last_index = len(people) - 1 - people[::-1].index(max_people)
    return last_index + 1


people = [3, 5, 2, 5, 4]
apartment = find_max_apartment(people)
print(f"Квартира с наибольшим числом жильцов: №{apartment}")
