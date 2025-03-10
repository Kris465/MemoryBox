def time_until_condition(hour, minute):
    
    if not (0 < hour <= 12 and 0 <= minute <= 59):
        return


    minute_coincide = (60 * hour) / 11
    time_coincide = (minute_coincide - minute) % 720


    m1 = (30 * hour - 90) / 5.5
    m2 = (30 * hour + 90) / 5.5
    m3 = (30 * hour - 270) / 5.5
    m4 = (30 * hour + 270) / 5.5

    possible_minutes = [m for m in [m1, m2, m3, m4] if m >= 0]
    if not possible_minutes:
        return

    m_perpendicular = min(possible_minutes)
    time_perpendicular = (m_perpendicular - minute) % 720

    return time_coincide, time_perpendicular


def get_user_input():

    while True:
        try:
            hour = int(input("Введите час (1-12): "))
            minute = int(input("Введите минуты (0-59): "))
            if 0 < hour <= 12 and 0 <= minute <= 59:
                return hour, minute
            else:
                print("Введены некорректные данные. Попробуйте снова.")
        except ValueError:
            print("Введены некорректные данные. Попробуйте снова.")


if __name__ == "__main__":

    hour, minute = get_user_input()


    time_coincide, time_perpendicular = time_until_condition(hour, minute)


    print(f"а) Время до совпадения стрелок: {time_coincide:.2f} минут")
    print(f"б) Время до перпендикулярного положения: {time_perpendicular:.2f} минут")
