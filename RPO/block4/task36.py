def traffic_light_color(t):
    t %= 5

    if t < 3:
        return 'зеленый'
    else:
        return 'красный'


t = 7.5
color = traffic_light_color(t)
print(color)
