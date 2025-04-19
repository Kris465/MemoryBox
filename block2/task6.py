def get_seconds():
    while True:
        try:
            n = int(input("Введите количество секунд: "))
            if n >= 0:
                return n
            else:
                print("Количество секунд должно быть неотрицательным числом.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

def calculate_time(seconds):
    hours_passed = seconds // 3600
    minutes_passed = (seconds % 3600) // 60
    seconds_passed = seconds % 60

    if hours_passed > 24:
        days_passed = hours_passed // 24
        hours_passed %= 24
        print(f"Прошло {days_passed} дней")
    
    print(f"Часов прошло: {hours_passed}")
    print(f"Минут прошло: {minutes_passed}")
    print(f"Секунд прошло: {seconds_passed}")

if __name__ == "__main__":
    seconds = get_seconds()
    calculate_time(seconds)
