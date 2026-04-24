def compare_athletes(athlete1_scores, athlete2_scores):
    """
    Функция сравнивает результаты двух спортсменов-десятиборцев.

    :param athlete1_scores: Список баллов первого спортсмена
    :param athlete2_scores: Список баллов второго спортсмена
    :return: Сообщение о победителе
    """
    assert len(athlete1_scores) == len(athlete2_scores) == 10, \
        "Ожидается 10 видов спорта!"

    total_score_athlete1 = sum(athlete1_scores)
    total_score_athlete2 = sum(athlete2_scores)

    if total_score_athlete1 > total_score_athlete2:
        return "Победил первый спортсмен!"
    elif total_score_athlete1 < total_score_athlete2:
        return "Победил второй спортсмен!"
    else:
        return "Ничья!"


athlete1_scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
athlete2_scores = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]

winner_message = compare_athletes(athlete1_scores, athlete2_scores)
print(winner_message)
