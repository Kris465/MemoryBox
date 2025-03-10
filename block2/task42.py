# TODO оформить файл в соответствии с PEP8
# Добавить пользовательский ввод.
# Добавить обработку пользовательского ввода.


def time_until_condition(h, m):

    if not (0 < h <= 12 and 0 <= m <= 59):
        return "Некорректные входные данные"
    


    m_coincide = (60 * h) / 11

    time_coincide = (m_coincide - m) % 720
    


    m1 = (30 * h - 90) / 5.5
    m2 = (30 * h + 90) / 5.5
    m3 = (30 * h - 270) / 5.5
    m4 = (30 * h + 270) / 5.5
    

    m_perpendicular = min(
        (x for x in [m1, m2, m3, m4] if x >= 0),
        default=None
    )
    
    if m_perpendicular is None:
        return "Невозможно найти перпендикулярное положение"
    

    time_perpendicular = (m_perpendicular - m) % 720
    
    return time_coincide, time_perpendicular


h = 3
m = 0
time_coincide, time_perpendicular = time_until_condition(h, m)
print(f"а) Время до совпадения стрелок: {time_coincide:.2f} минут")
print(f"б) Время до перпендикулярного положения: {time_perpendicular:.2f} минут")
