def next_coincidence(h, m):
    t = ((11 * m - 330 * h) % 660) / 11
    return t


def next_perpendicularity(h, m):
    t1 = ((11 * m - 300 * h) % 660) / 11
    t2 = ((11 * m - 390 * h) % 660) / 11
    return min(t1, t2)


h = 3
m = 25

coincidence_time = next_coincidence(h, m)
perpendicularity_time = next_perpendicularity(h, m)

print(f"Время до совпадения стрелок: {coincidence_time:.2f} минут")
print(f"Время до \
      перпендикулярности стрелок: {perpendicularity_time:.2f} минут")
