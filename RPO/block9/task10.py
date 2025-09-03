
def find_longest_and_shortest(cities):

    sorted_cities = sorted(cities, key=len)

    shortest_city = sorted_cities[0]

    longest_city = sorted_cities[-1]

    return longest_city, shortest_city


cities = ["Москва", "Санкт-Петербург", "Краснодар"]


longest_city, shortest_city = find_longest_and_shortest(cities)
print(f"Самое длинное название: {longest_city}")
print(f"Самое короткое название: {shortest_city}")
