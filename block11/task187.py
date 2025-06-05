grades = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
          4, 3, 4, 5, 4, 3, 2, 4, 3, 2, 3, 4]


index_of_non_five = grades.index(next((x for x in grades if x != 5),
                                      grades[-1] + 1))

count_fives = index_of_non_five

print("Количество пятёрок:", count_fives)
