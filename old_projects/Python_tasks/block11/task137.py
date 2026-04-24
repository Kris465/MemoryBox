
scores = [15, 20, 18, 22, 19, 21, 17, 23, 16, 24,
          20, 22, 19, 25, 21, 23, 20, 24, 18, 26]


top_score = float('-inf')
second_top_score = float('-inf')

for score in scores:
    if score > top_score:
        second_top_score = top_score
        top_score = score
    elif top_score > score > second_top_score:
        second_top_score = score

print("Первое место (максимальные очки):", top_score)
print("Второе место:", second_top_score)
