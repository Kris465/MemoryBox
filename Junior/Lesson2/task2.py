def favorite_cartoons():
    cartoons = []
    while True:
        cartoon = input(
            "Введите название мультфильма (или 'стоп' для завершения): ")
        if cartoon.lower() == 'стоп':
            break
        cartoons.append(cartoon)

    print("Ваши любимые мультфильмы:")
    for cartoon in cartoons:
        print(cartoon)


favorite_cartoons()
