def sum_top_three(scores):
    return sum(sorted(scores, reverse=True)[:3])


scores = [50, 60, 70, 80, 90]
result = sum_top_three(scores)
print(f"Сумма очков трех лучших команд: {result}")
