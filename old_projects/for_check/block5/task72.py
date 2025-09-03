def calculate_speed(initial_speed, increment, seconds):
    speed = initial_speed
    for _ in range(seconds):
        speed += speed * increment / 100
    return speed


initial_speed = 10
increment = 10
seconds = 10
final_speed = calculate_speed(initial_speed, increment, seconds)
print("Финальная скорость капли: {:.2f} км/ч".format(final_speed))
