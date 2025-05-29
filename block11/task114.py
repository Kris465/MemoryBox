
scores = [/* вставьте сюда оценки судей, например: 9.5, 8.7, 9.0, ... */]


max_score = max(scores)
min_score = min(scores)


scores.remove(max_score)
scores.remove(min_score)

average_score = sum(scores) / len(scores)

print("Среднее арифметическое после удаления наибольшей и наименьшей оценки:", average_score)