def skating_score(scores):
    if len(scores) < 3:
        return 0.0
    copy = list(scores)
    copy.remove(max(copy))
    copy.remove(min(copy))
    return sum(copy) / len(copy)


scores = [9.5, 8.0, 9.0, 9.5, 8.5]
score = skating_score(scores)
print(f"Оценка спортсмена: {score:.2f}")
