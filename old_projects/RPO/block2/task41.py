import math


def calculate_minute_angle_and_time(angle_y):

    if not (0 < angle_y <= 2 * math.pi):
        return

    total_minutes = (angle_y / (2 * math.pi)) * 12 * 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    theta_m = 12 * angle_y
    theta_m %= 2 * math.pi

    return theta_m, hours, minutes


def get_user_input():

    while True:
        try:
            angle_y = float(input("Введите угол y в радианах (0 < y ≤ 2π): "))
            if 0 < angle_y <= 2 * math.pi:
                return angle_y
            else:
                print("Угол y должен быть в диапазоне \
                    (0, 2π]. Попробуйте снова.")
        except ValueError:
            print("Введены некорректные данные. Попробуйте снова.")


if __name__ == "__main__":

    angle_y = get_user_input()

    theta_m, hours, minutes = calculate_minute_angle_and_time(angle_y)

    if isinstance(theta_m, str):
        print(theta_m)
    else:
        print(f"Угол минутной стрелки: {theta_m:.2f} радиан")
        print(f"Количество полных часов: {hours}")
        print(f"Количество полных минут: {minutes}")
